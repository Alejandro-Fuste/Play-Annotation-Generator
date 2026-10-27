# Play-Annotation-Generator Annotation Review — Counter_155

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_155`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | LB1 | defense | `9` | `8` |
| ✅ EXACT | `Action_PlaySideFakeStep` | LG | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LG | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 30 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `16` | `15` | 31 | START | 31 | 36 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `14` | `13` | 37 | START | 37 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `16` | `15` | 37 | START | 37 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `17` | `16` | 37 | START | 37 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `22` | `21` | 37 | START | 37 | 85 |
| ✅ EXACT | `Action_PullLeadBlock` | LB1 | `9` | `8` | 37 | START | 37 | 104 |
| ✅ EXACT | `Action_PlaySideFakeStep` | LG | `10` | `9` | 42 | START | 42 | 72 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `18` | `17` | 42 | END | 31 | 42 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `18` | `17` | 56 | START | 56 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LG | `10` | `9` | 73 | START | 73 | 112 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 104 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `4`</summary>

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
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 208 | 178 | inferred_complete_timeline |
| `Action_None` | 211 | 239 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 73 | 43 | inferred_complete_timeline |
| `Action_None` | 77 | 93 | 17 | inferred_complete_timeline |
| `Action_None` | 96 | 113 | 18 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 42 | 72 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 73 | 112 | 40 | inferred_complete_timeline |
| `Action_BallCarry` | 117 | 228 | 112 | inferred_complete_timeline |
| `Action_BallCarry` | 230 | 231 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 222 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 239 | 209 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 198 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 238 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 83 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 175 | 145 | inferred_complete_timeline |
| `Action_None` | 178 | 182 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 37 | 104 | 68 | inferred_complete_timeline |
| `Action_None` | 105 | 137 | 33 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 150 | 5 | inferred_complete_timeline |
| `Action_None` | 154 | 228 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 54 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 147 | 117 | inferred_complete_timeline |
| `Action_None` | 154 | 214 | 61 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–116 | 116 | 4 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–112 | 113 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–239 | 225 | 6 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–60 | 59 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–237 | 238 | 5 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–168 | 148 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–239 | 201 | 5 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–60 | 61 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 0–239 | 237 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 65–116 | 52 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 71–239 | 167 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 87–239 | 137 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 98–225 | 127 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 115–116 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 130–239 | 110 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 146–195 | 43 | 4 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 152–225 | 74 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 154–239 | 75 | 2 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 155–239 | 78 | 3 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 165–239 | 75 | 1 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 196–199 | 4 | 1 | Undefined position; Undefined team |
| `34` | `36` | Position_Unknown | Team_Unknown | 204–205 | 2 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 219–239 | 21 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 312: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [31-238] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-208] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-222] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-147] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-214] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-73] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-93] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-113] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-198] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-228] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [73-112] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [117-228] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [230-231] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-54] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-175] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-83] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-113] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-112] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-117] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [37-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [47-60] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-237] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-145] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-95] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-60] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [37-85] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-116] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-117] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-124] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-131] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-225] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-160] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-174] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-195] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-161] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-205] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>