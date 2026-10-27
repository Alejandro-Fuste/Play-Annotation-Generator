# Play-Annotation-Generator Annotation Review — Counter_327

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_327`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `15` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 30 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 31 | START | 31 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `16` | `15` | 34 | START | 34 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `19` | `18` | 34 | START | 34 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `21` | `20` | 34 | START | 50 | 77 |
| ✅ EXACT | `Action_PullBlock` | RG | `22` | `21` | 34 | START | 34 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `15` | `14` | 34 | START | 34 | 77 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 45 | END | 31 | 45 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `17` | 56 | START | 56 | 75 |
| ✅ EXACT | `Action_BallCarry` | RB | `17` | `16` | 76 | START | 76 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 124 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 45 | 15 | inferred_complete_timeline |
| `Action_None` | 46 | 55 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 56 | 75 | 20 | inferred_complete_timeline |
| `Action_None` | 76 | 93 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 75 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 76 | 239 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 152 | 122 | inferred_complete_timeline |
| `Action_None` | 173 | 189 | 17 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 239 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 239 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 34 | 77 | 44 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 82 | 85 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_DownBlock` | 34 | 81 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 86 | 88 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 101 | 107 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 46 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_BallSnap` | 31 | 45 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 50 | 77 | 28 | inferred_complete_timeline |
| `Action_DownBlock` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 163 | 7 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 172 | 3 | inferred_complete_timeline |
| `Action_None` | 180 | 239 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PullBlock` | 34 | 79 | 46 | inferred_complete_timeline |
| `Action_None` | 151 | 152 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_DownBlock` | 34 | 59 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 61 | 124 | 64 | inferred_complete_timeline |
| `Action_None` | 125 | 239 | 115 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 79 | 49 | inferred_complete_timeline |
| `Action_None` | 120 | 125 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 61 | 31 | inferred_complete_timeline |
| `Action_None` | 63 | 77 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 83 | 53 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_None` | 194 | 197 | 4 | inferred_complete_timeline |
| `Action_None` | 200 | 239 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 77 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 88 | 58 | inferred_complete_timeline |
| `Action_None` | 90 | 96 | 7 | inferred_complete_timeline |
| `Action_None` | 106 | 123 | 18 | inferred_complete_timeline |
| `Action_None` | 133 | 136 | 4 | inferred_complete_timeline |
| `Action_None` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_None` | 149 | 220 | 72 | inferred_complete_timeline |
| `Action_None` | 222 | 224 | 3 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 129 | 99 | inferred_complete_timeline |
| `Action_None` | 132 | 137 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 164 | 134 | inferred_complete_timeline |
| `Action_None` | 167 | 214 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 239 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 183 | 153 | inferred_complete_timeline |
| `Action_None` | 185 | 192 | 8 | inferred_complete_timeline |
| `Action_None` | 196 | 200 | 5 | inferred_complete_timeline |
| `Action_None` | 204 | 211 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 239 | 209 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 141–239 | 95 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 145–156 | 12 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 171–239 | 62 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 171–239 | 69 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 174–239 | 65 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 182–239 | 58 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 186–239 | 51 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 204–239 | 32 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 217–239 | 23 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 225–239 | 14 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 233–239 | 7 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 233–239 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '18' (RT) duration 91 frames exceeds threshold 90 frames [start=34, end=124].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (C) duration 91 frames exceeds threshold 90 frames [start=34, end=124].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [31–45], lower_priority='Action_DownBlock' annotated_start=34, effective_Action_DownBlock_start=46.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '21' (RG) duration 91 frames exceeds threshold 90 frames [start=34, end=124].
- ⚠️ Action 'Action_None' range [31-152] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-189] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-79] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-61] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-77] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-77] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-164] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-214] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-88] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-96] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-123] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-83] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-137] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-183] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-192] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-211] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [34-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [82-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [34-81] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [86-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [101-107] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [76-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [34-59] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-46] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [31-45] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [50-77] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [120-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-163] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [34-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-173] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-195] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-239] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>