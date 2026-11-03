# Play-Annotation-Generator Annotation Review — Post10to15_57

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_57`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 102
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_RunPostRoute` | WR1 | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_BallSnap` | LG | `17` | `17` | 7 | START | 7 | 9 |
| ✅ EXACT | `Action_PassBlock` | LG | `17` | `17` | 10 | START | 10 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `18` | `18` | 10 | START | 10 | 46 |
| ✅ EXACT | `Action_PassBlock` | C | `21` | `21` | 10 | START | 10 | 120 |
| ✅ EXACT | `Action_PassBlock` | RT | `3` | `3` | 10 | START | 10 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `9` | `9` | 10 | START | 10 | 36 |
| ✅ EXACT | `Action_RunPostRoute` | WR1 | `7` | `7` | 21 | START | 21 | 210 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 21 | END | 7 | 21 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 90 | START | 90 | 98 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 7 | 21 | 15 | inferred_complete_timeline |
| `Action_None` | 22 | 89 | 68 | inferred_complete_timeline |
| `Action_ThrowPass` | 90 | 98 | 9 | inferred_complete_timeline |
| `Action_None` | 99 | 169 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 120 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_RunPostRoute` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 207 | 201 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 120 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 173 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 46 | 37 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 103 | 51 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 154 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 206 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 7 | 9 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 193 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 120 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 36 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 43 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 52 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 120 | 111 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 147 | 141 | inferred_complete_timeline |
| `Action_None` | 151 | 178 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 36 | 30 | inferred_complete_timeline |
| `Action_None` | 38 | 89 | 52 | inferred_complete_timeline |
| `Action_None` | 93 | 162 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 184 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 65 | 59 | inferred_complete_timeline |
| `Action_None` | 67 | 101 | 35 | inferred_complete_timeline |
| `Action_None` | 117 | 120 | 4 | inferred_complete_timeline |
| `Action_None` | 179 | 196 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 120 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 114 | 108 | inferred_complete_timeline |
| `Action_None` | 116 | 120 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 130 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 120 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 120 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 191 | 185 | inferred_complete_timeline |
| `Action_None` | 193 | 210 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 35–116 | 36 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 42–210 | 93 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 45–52 | 7 | 2 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 55–210 | 76 | 3 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 71–72 | 2 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 82–210 | 48 | 4 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 100–101 | 2 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 102–210 | 109 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 113–115 | 3 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 121–198 | 78 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 121–179 | 59 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 121–210 | 90 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 121–210 | 90 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 121–192 | 72 | 1 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 121–210 | 90 | 1 | Undefined position; Undefined team |
| `37` | `40` | Position_Unknown | Team_Unknown | 121–210 | 79 | 2 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 126–133 | 8 | 1 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 163–167 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 65 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [7-207] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-147] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-178] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-184] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [21-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-36] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-43] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-52] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-130] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-191] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-193] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-46] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-103] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [105-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [156-206] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-36] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-89] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-120] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-40] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-116] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-43] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-48] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-52] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-58] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-179] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-198] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-179] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-192] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-127] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-210] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-133] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '39' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.

</details>