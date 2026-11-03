# Play-Annotation-Generator Annotation Review — StopAndGo_49

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_49`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 67
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB1 | defense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_VerticalStem` | WR3 | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_SellStop` | WR3 | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `4` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 21 |
| ✅ EXACT | `Action_BallSnap` | CB1 | `13` | `13` | 22 | START | 22 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `11` | `11` | 25 | START | 25 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `17` | `17` | 25 | START | 25 | 51 |
| ✅ EXACT | `Action_PassBlock` | RG | `19` | `19` | 25 | START | 25 | 191 |
| ✅ EXACT | `Action_PassBlock` | LT | `20` | `20` | 25 | START | 25 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `3` | `3` | 25 | START | 25 | 58 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 38 | END | 22 | 38 |
| ✅ EXACT | `Action_VerticalStem` | WR3 | `0` | `0` | 38 | START | 38 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_SellStop` | WR3 | `0` | `0` | 73 | START | 73 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | `0` | `0` | 96 | START | 96 | 208 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 101 | START | 101 | 113 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 38 | 17 | inferred_complete_timeline |
| `Action_None` | 39 | 100 | 62 | inferred_complete_timeline |
| `Action_ThrowPass` | 101 | 113 | 13 | inferred_complete_timeline |
| `Action_None` | 114 | 171 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 188 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 70 | 49 | inferred_complete_timeline |
| `Action_None` | 73 | 87 | 15 | inferred_complete_timeline |
| `Action_None` | 90 | 117 | 28 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 137 | 11 | inferred_complete_timeline |
| `Action_None` | 139 | 142 | 4 | inferred_complete_timeline |
| `Action_None` | 144 | 176 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 162 | 141 | inferred_complete_timeline |
| `Action_None` | 165 | 239 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 238 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_VerticalStem` | 38 | 72 | 35 | inferred_complete_timeline |
| `Action_SellStop` | 73 | 77 | 5 | inferred_complete_timeline |
| `Action_SellStop` | 79 | 95 | 17 | inferred_complete_timeline |
| `Action_RunGoRoute` | 96 | 208 | 113 | inferred_complete_timeline |
| `Action_RunGoRoute` | 214 | 216 | 3 | inferred_complete_timeline |
| `Action_RunGoRoute` | 221 | 239 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 167 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 51 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 176 | 120 | inferred_complete_timeline |
| `Action_PassBlock` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 58 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 136 | 76 | inferred_complete_timeline |
| `Action_PassBlock` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 151 | 172 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 176 | 178 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 180 | 185 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 191 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 132 | 108 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 180 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 88 | 67 | inferred_complete_timeline |
| `Action_None` | 92 | 96 | 5 | inferred_complete_timeline |
| `Action_None` | 98 | 111 | 14 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 190 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 185 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 86 | 65 | inferred_complete_timeline |
| `Action_None` | 108 | 111 | 4 | inferred_complete_timeline |
| `Action_None` | 114 | 182 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 206 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 233 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 22 | 38 | 17 | inferred_complete_timeline |
| `Action_None` | 39 | 239 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 92 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 222 | 201 | inferred_complete_timeline |
| `Action_None` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 223 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 36–37 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 104–239 | 135 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 113–116 | 4 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 126–169 | 25 | 2 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 179–186 | 8 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 192–195 | 4 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 196–204 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (6 segments found)
- ⚠️ Ambiguous match for action `Action_SellStop` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `0` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 51 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_SellStop' range [73-77] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [96-208] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [214-216] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [221-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-88] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-96] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-111] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-190] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-58] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-136] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [148-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [151-172] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [176-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [180-185] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-70] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-87] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-117] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-176] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-162] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-222] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-185] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-238] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-86] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-111] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-182] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-233] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-180] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-206] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-223] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-51] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-176] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [178-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-171] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-191] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-167] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-188] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-37] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-112] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-186] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-204] for track '28' has 2 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>