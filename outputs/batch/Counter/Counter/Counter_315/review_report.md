# Play-Annotation-Generator Annotation Review — Counter_315

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_315`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `19` | `18` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 87 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 43 | START | 43 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `14` | `13` | 46 | START | 46 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `19` | `18` | 46 | START | 46 | 63 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `20` | `19` | 46 | START | 59 | 89 |
| ✅ EXACT | `Action_PullBlock` | LG | `22` | `21` | 46 | START | 46 | 127 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `7` | `6` | 46 | START | 46 | 127 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 58 | END | 43 | 58 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `12` | 65 | START | 65 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `8` | 88 | START | 88 | 121 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 127 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_SnapReceive` | 43 | 58 | 16 | inferred_complete_timeline |
| `Action_None` | 59 | 64 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 65 | 87 | 23 | inferred_complete_timeline |
| `Action_None` | 88 | 159 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_BallCarry` | 88 | 121 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 127 | 219 | 93 | inferred_complete_timeline |
| `Action_BallCarry` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 236 | 194 | inferred_complete_timeline |
| `Action_None` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 226 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 109 | 67 | inferred_complete_timeline |
| `Action_None` | 115 | 228 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 46 | 127 | 82 | inferred_complete_timeline |
| `Action_None` | 128 | 239 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 166 | 124 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_None` | 173 | 223 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PullBlock` | 46 | 127 | 82 | inferred_complete_timeline |
| `Action_None` | 128 | 218 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_BallSnap` | 43 | 58 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 59 | 89 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_DownBlock` | 46 | 95 | 50 | inferred_complete_timeline |
| `Action_DownBlock` | 97 | 110 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 115 | 122 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 124 | 127 | 4 | inferred_complete_timeline |
| `Action_None` | 128 | 238 | 111 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 152 | 110 | inferred_complete_timeline |
| `Action_None` | 155 | 239 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 89 | 47 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 239 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 63 | 21 | inferred_complete_timeline |
| `Action_None` | 68 | 96 | 29 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 152 | 14 | inferred_complete_timeline |
| `Action_None` | 155 | 210 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 125 | 83 | inferred_complete_timeline |
| `Action_None` | 130 | 134 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 111 | 69 | inferred_complete_timeline |
| `Action_None` | 123 | 166 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 239 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 239 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 186 | 144 | inferred_complete_timeline |
| `Action_None` | 190 | 213 | 24 | inferred_complete_timeline |
| `Action_None` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 80 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 124 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–66 | 66 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 76–219 | 141 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 84–239 | 108 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 85–92 | 4 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 87–239 | 153 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 93–180 | 7 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 97–133 | 37 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 114–239 | 125 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 121–239 | 119 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 140–239 | 100 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 144–239 | 83 | 4 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 148–164 | 11 | 2 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 186–239 | 40 | 5 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 210–211 | 2 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (3 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `20` (C): Annotated start 46 != Inferred start 59
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 632: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [43–58], lower_priority='Action_DownBlock' annotated_start=46, effective_Action_DownBlock_start=59.
- ⚠️ Action 'Action_None' range [43-89] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-236] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-152] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-226] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-109] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-228] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-239] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-125] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [88-121] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [127-219] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-166] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-223] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-124] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [46-95] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [97-110] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [115-122] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-238] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-186] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-213] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-111] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-166] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [46-63] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [65-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [59-89] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-63] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-96] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-210] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-218] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-130] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-219] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-93] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-134] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-133] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-158] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-229] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-239] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-155] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-193] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-228] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>