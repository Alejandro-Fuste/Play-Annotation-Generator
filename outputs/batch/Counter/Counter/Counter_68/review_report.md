# Play-Annotation-Generator Annotation Review — Counter_68

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_68`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `16` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `4` | `3` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 15 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 53 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `14` | 54 | START | 54 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `16` | `14` | 56 | START | 71 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `6` | `5` | 56 | START | 56 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `4` | `3` | 56 | START | 56 | 77 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `7` | `6` | 56 | START | 56 | 73 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 67 | END | 54 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `9` | `8` | 77 | START | 77 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `4` | `3` | 96 | START | 96 | 106 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 136 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–93
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_SnapReceive` | 54 | 67 | 14 | inferred_complete_timeline |
| `Action_None` | 68 | 76 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 77 | 86 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 92 | 93 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 55 | 47 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 56 | 73 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_DownBlock` | 56 | 70 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 99 | 102 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 117 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 53 | 47 | inferred_complete_timeline |
| `Action_None` | 54 | 85 | 32 | inferred_complete_timeline |
| `Action_None` | 87 | 134 | 48 | inferred_complete_timeline |
| `Action_None` | 151 | 210 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 15–111
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 53 | 39 | inferred_complete_timeline |
| `Action_BallSnap` | 54 | 66 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 77 | 101 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 105 | 111 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 36 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 53 | 16 | inferred_complete_timeline |
| `Action_None` | 54 | 63 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 238 | 185 | inferred_complete_timeline |

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
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 112 | 59 | inferred_complete_timeline |
| `Action_None` | 121 | 124 | 4 | inferred_complete_timeline |
| `Action_None` | 142 | 239 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 154 | 101 | inferred_complete_timeline |
| `Action_None` | 157 | 176 | 20 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 193 | 239 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 89 | 36 | inferred_complete_timeline |
| `Action_None` | 93 | 100 | 8 | inferred_complete_timeline |
| `Action_None` | 102 | 108 | 7 | inferred_complete_timeline |
| `Action_None` | 114 | 116 | 3 | inferred_complete_timeline |
| `Action_None` | 120 | 124 | 5 | inferred_complete_timeline |
| `Action_None` | 127 | 185 | 59 | inferred_complete_timeline |
| `Action_None` | 188 | 239 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 112 | 59 | inferred_complete_timeline |
| `Action_None` | 120 | 133 | 14 | inferred_complete_timeline |
| `Action_None` | 144 | 151 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 93 | 40 | inferred_complete_timeline |
| `Action_None` | 99 | 181 | 83 | inferred_complete_timeline |
| `Action_None` | 183 | 226 | 44 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 143 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 203 | 150 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–239 | 226 | 6 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 67–120 | 49 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 74–82 | 9 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 90–108 | 16 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 94–239 | 132 | 2 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 109–239 | 130 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 114–239 | 110 | 4 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 146–195 | 50 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 147–239 | 61 | 3 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 156–239 | 81 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 160–226 | 62 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 161–216 | 56 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 174–239 | 66 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 201–207 | 7 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 203–239 | 37 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 217–225 | 5 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 218–236 | 19 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 223–239 | 14 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 227–239 | 13 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 236–238 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 138: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [54–67], lower_priority='Action_DownBlock' annotated_start=56, effective_Action_DownBlock_start=68.
- ⚠️ Action 'Action_None' range [54-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-176] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-203] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-112] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [56-77] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [82-84] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [96-106] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-93] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-181] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-226] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [56-70] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [99-102] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [107-117] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [56-73] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-133] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-151] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [77-86] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [92-93] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-238] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-89] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-100] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-185] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-134] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-63] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [54-66] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [71-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [77-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [105-111] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-120] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-82] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-108] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-239] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-192] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-195] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-154] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-196] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-192] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-226] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-216] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-207] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-236] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-232] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>