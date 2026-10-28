# Play-Annotation-Generator Annotation Review — Draw_95

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_95`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `15` | `14` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 21 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `15` | `14` | 19 | START | 24 | 35 |
| ✅ EXACT | `Action_PassBlock` | RT | `12` | `11` | 22 | START | 22 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `2` | `1` | 22 | START | 22 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `4` | `3` | 22 | START | 22 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `5` | `4` | 22 | START | 22 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `8` | `7` | 22 | START | 22 | 45 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 35 | END | 19 | 35 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `11` | `10` | 39 | START | 39 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `11` | `10` | 77 | START | 77 | 214 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 101 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 35 | 17 | inferred_complete_timeline |
| `Action_None` | 36 | 38 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 39 | 76 | 38 | inferred_complete_timeline |
| `Action_BallCarry` | 77 | 214 | 138 | inferred_complete_timeline |
| `Action_BallCarry` | 217 | 224 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 47 | 29 | inferred_complete_timeline |
| `Action_None` | 49 | 60 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 38 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 77 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 101 | 21 | inferred_complete_timeline |
| `Action_None` | 102 | 145 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 56 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 69 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 83 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 33 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 101 | 61 | inferred_complete_timeline |
| `Action_None` | 102 | 214 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 45 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 101 | 55 | inferred_complete_timeline |
| `Action_None` | 102 | 180 | 79 | inferred_complete_timeline |
| `Action_None` | 182 | 191 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 101 | 80 | inferred_complete_timeline |
| `Action_None` | 102 | 248 | 147 | inferred_complete_timeline |
| `Action_None` | 251 | 256 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 389 | 371 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 77 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 123 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 109 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 389 | 371 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 83 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 88 | 70 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 24–148 | 125 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 47–159 | 112 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 62–261 | 174 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 68–236 | 169 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 85–97 | 8 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 94–113 | 20 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 105–389 | 282 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 110–319 | 190 | 7 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 120–167 | 48 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 122–389 | 249 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 175–302 | 107 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 176–389 | 213 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 177–389 | 212 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 239–240 | 2 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 254–384 | 126 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 261–297 | 6 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 323–324 | 2 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 326–389 | 64 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 369–389 | 21 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `15` (Position_Unknown): Annotated start 19 != Inferred start 24
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 60 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PassBlock' range [22-38] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-77] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-145] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-88] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-56] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-69] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [78-79] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-83] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-33] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-214] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-123] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-45] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-191] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-83] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakePassDroptoHandoff' range [39-76] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [77-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [217-224] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-248] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-256] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-47] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-77] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-159] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-261] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-236] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-157] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-165] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-184] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-275] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-319] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-167] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-213] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-272] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-381] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-389] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-382] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-366] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-378] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '31' has 1 frames without a visible bounding box.
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

</details>