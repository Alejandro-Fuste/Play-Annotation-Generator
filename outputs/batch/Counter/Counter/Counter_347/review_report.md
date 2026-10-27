# Play-Annotation-Generator Annotation Review — Counter_347

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_347`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PullLeadBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `13` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 46 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 47 | START | 47 | 59 |
| ✅ EXACT | `Action_DownBlock` | LG | `22` | `21` | 50 | START | 50 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `21` | `20` | 50 | START | 60 | 83 |
| ✅ EXACT | `Action_PullLeadBlock` | RG | `20` | `19` | 50 | START | 50 | 67 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 59 | END | 47 | 59 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `8` | 66 | START | 66 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `7` | 81 | START | 81 | 150 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 123 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 59 | 13 | inferred_complete_timeline |
| `Action_None` | 60 | 65 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 66 | 80 | 15 | inferred_complete_timeline |
| `Action_None` | 81 | 194 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 80 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 81 | 150 | 70 | inferred_complete_timeline |
| `Action_BallCarry` | 152 | 201 | 50 | inferred_complete_timeline |
| `Action_BallCarry` | 203 | 208 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 98 | 52 | inferred_complete_timeline |
| `Action_None` | 102 | 210 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 210 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 210 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 210 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 210 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 93 | 47 | inferred_complete_timeline |
| `Action_None` | 98 | 115 | 18 | inferred_complete_timeline |
| `Action_None` | 117 | 210 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_DownBlock` | 50 | 123 | 74 | inferred_complete_timeline |
| `Action_None` | 124 | 133 | 10 | inferred_complete_timeline |
| `Action_None` | 136 | 210 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_BallSnap` | 47 | 59 | 13 | inferred_complete_timeline |
| `Action_PullBlock` | 60 | 83 | 24 | inferred_complete_timeline |
| `Action_PullBlock` | 86 | 93 | 8 | inferred_complete_timeline |
| `Action_PullBlock` | 108 | 111 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 50 | 67 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 210 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 88 | 42 | inferred_complete_timeline |
| `Action_None` | 90 | 210 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 65 | 19 | inferred_complete_timeline |
| `Action_None` | 83 | 90 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 108 | 62 | inferred_complete_timeline |
| `Action_None` | 113 | 123 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 120 | 74 | inferred_complete_timeline |
| `Action_None` | 129 | 210 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 165 | 119 | inferred_complete_timeline |
| `Action_None` | 168 | 178 | 11 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 210 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 123 | 77 | inferred_complete_timeline |
| `Action_None` | 126 | 130 | 5 | inferred_complete_timeline |
| `Action_None` | 132 | 210 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 210 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 210 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 115 | 69 | inferred_complete_timeline |
| `Action_None` | 122 | 133 | 12 | inferred_complete_timeline |
| `Action_None` | 136 | 162 | 27 | inferred_complete_timeline |
| `Action_None` | 165 | 210 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 210 | 164 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 67–76 | 10 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 90–210 | 121 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 138–210 | 61 | 6 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 148–161 | 14 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 155–210 | 56 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 173–210 | 38 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [47–59], lower_priority='Action_PullBlock' annotated_start=50, effective_Action_PullBlock_start=60.
- ⚠️ Action 'Action_None' range [47-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-123] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [81-150] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [152-201] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-208] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-194] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-65] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-90] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-98] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-133] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-162] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-108] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-123] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-115] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [50-67] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [60-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [86-93] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [108-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-76] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-173] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-161] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '27' has 1 frames without a visible bounding box.
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

</details>