# Play-Annotation-Generator Annotation Review — Draw_72

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_72`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 2
- **Action Segments:** 66
- **Validation Warnings:** 71
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `1` | `0` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `9` | `8` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_FakePassDroptoHandoff` | QB | offense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 72 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `3` | `2` | 70 | START | 70 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `1` | `0` | 73 | START | 73 | 144 |
| ✅ EXACT | `Action_PassBlock` | LG | `12` | `11` | 73 | START | 73 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `14` | `13` | 73 | START | 73 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `9` | `8` | 73 | START | 73 | 101 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `8` | `7` | 85 | END | 70 | 83 |
| ❌ MISSING SEGMENT | `Action_FakePassDroptoHandoff` | QB | `8` | `7` | 88 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | `8` | `7` | 107 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 148 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_SnapReceive` | 70 | 83 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 225 | 156 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 101 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 104 | 141 | 38 | inferred_complete_timeline |
| `Action_None` | 168 | 239 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 148 | 76 | inferred_complete_timeline |
| `Action_None` | 149 | 239 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 144 | 72 | inferred_complete_timeline |
| `Action_PassBlock` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 149 | 1 | inferred_complete_timeline |
| `Action_None` | 156 | 163 | 8 | inferred_complete_timeline |
| `Action_None` | 167 | 187 | 21 | inferred_complete_timeline |
| `Action_None` | 209 | 212 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 90 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 107 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 114 | 116 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 148 | 30 | inferred_complete_timeline |
| `Action_None` | 149 | 239 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 99 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 185 | 116 | inferred_complete_timeline |
| `Action_None` | 187 | 205 | 19 | inferred_complete_timeline |
| `Action_None` | 207 | 239 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 168 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 115 | 46 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_None` | 124 | 126 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 96 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 117 | 48 | inferred_complete_timeline |
| `Action_None` | 119 | 122 | 4 | inferred_complete_timeline |
| `Action_None` | 127 | 227 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 128 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–239 | 240 | 3 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 6–14 | 9 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 142–239 | 98 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 145–150 | 6 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 157–239 | 77 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 170–239 | 70 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 186–239 | 54 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 188–236 | 49 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 200–239 | 40 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 205–239 | 35 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 214–239 | 26 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 221–239 | 19 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 222–239 | 18 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 223–239 | 17 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 233–239 | 7 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | 48 | 54 | 7 | 100.0% | None |
| `16` | `19` | 98 | 100 | 3 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (2 segments found)
- ❌ Missing segment for action `Action_FakePassDroptoHandoff` on target `8` (QB)
- ❌ Missing segment for action `Action_BallCarry` on target `8` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 33 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 144: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_FakePassDroptoHandoff' for track '7' has invalid range: start=88, end=83. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '7' has invalid range: start=107, end=83. Clamping end to start.
- ⚠️ Action 'Action_PassBlock' range [73-144] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '0' starts at frame 149, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [149-149] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-163] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-187] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-99] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-128] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-96] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-185] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-205] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [70-83] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-101] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [104-141] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-225] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-227] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-90] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-107] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [111-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [114-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-148] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-14] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-236] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>