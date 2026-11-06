# Play-Annotation-Generator Annotation Review — PuntCoverage_112

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_112`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 61
- **Ball Tracks:** 0
- **Action Segments:** 209
- **Validation Warnings:** 300
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 164
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `8` | `Group` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `57` | `35` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `57` | `35` |
| ✅ COLLECTIVE TACKLE | `Action_Tackle` | Group | defense | `group` | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `0` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `1` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `2` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `3` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `5` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `7` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `8` | `Group` | 0 | START | 0 | 20 |
| ✅ EXACT | `Action_PuntBall` | Punter | `0` | `0` | 64 | START | 64 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchPunt` | Position_Unknown | `57` | `35` | 177 | START | 177 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `57` | `35` | 193 | START | 193 | 200 |
| ✅ COLLECTIVE EVENT | `Action_Tackle` | Group | `group` | N/A | 251 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–30
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 30 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 151 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 158 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 165 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 176 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 195 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–282
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 69 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 85 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 101 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 109 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 193 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 215 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 225 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 242 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 282 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 127 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 139 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PuntBall` | 64 | 82 | 19 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 31 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 67 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 110 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 113 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 90 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 111 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 123 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 135 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 153 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 172 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 190 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 193 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 52 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 32 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 48 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 108 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 133 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 158 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 299 | 140 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 2–25 | 18 | 2 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 3–108 | 22 | 5 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 5–181 | 90 | 7 | Undefined position; Undefined team |
| `13` | `20` | Position_Unknown | Team_Unknown | 15–162 | 70 | 9 | Undefined position; Undefined team |
| `14` | `22` | Position_Unknown | Team_Unknown | 30–66 | 17 | 4 | Undefined position; Undefined team |
| `15` | `27` | Position_Unknown | Team_Unknown | 38–134 | 95 | 2 | Undefined position; Undefined team |
| `16` | `31` | Position_Unknown | Team_Unknown | 48–83 | 34 | 3 | Undefined position; Undefined team |
| `17` | `32` | Position_Unknown | Team_Unknown | 48–106 | 57 | 2 | Undefined position; Undefined team |
| `18` | `33` | Position_Unknown | Team_Unknown | 52–53 | 2 | 1 | Undefined position; Undefined team |
| `19` | `34` | Position_Unknown | Team_Unknown | 52–100 | 26 | 4 | Undefined position; Undefined team |
| `20` | `36` | Position_Unknown | Team_Unknown | 59–81 | 23 | 1 | Undefined position; Undefined team |
| `21` | `37` | Position_Unknown | Team_Unknown | 65–66 | 2 | 1 | Undefined position; Undefined team |
| `22` | `39` | Position_Unknown | Team_Unknown | 67–230 | 162 | 3 | Undefined position; Undefined team |
| `23` | `41` | Position_Unknown | Team_Unknown | 72–299 | 177 | 6 | Undefined position; Undefined team |
| `24` | `42` | Position_Unknown | Team_Unknown | 73–74 | 2 | 1 | Undefined position; Undefined team |
| `25` | `43` | Position_Unknown | Team_Unknown | 79–285 | 189 | 6 | Undefined position; Undefined team |
| `26` | `44` | Position_Unknown | Team_Unknown | 82–169 | 56 | 4 | Undefined position; Undefined team |
| `27` | `45` | Position_Unknown | Team_Unknown | 83–141 | 59 | 1 | Undefined position; Undefined team |
| `28` | `48` | Position_Unknown | Team_Unknown | 92–299 | 189 | 5 | Undefined position; Undefined team |
| `29` | `49` | Position_Unknown | Team_Unknown | 92–131 | 33 | 4 | Undefined position; Undefined team |
| `30` | `50` | Position_Unknown | Team_Unknown | 93–128 | 32 | 2 | Undefined position; Undefined team |
| `31` | `52` | Position_Unknown | Team_Unknown | 106–159 | 53 | 2 | Undefined position; Undefined team |
| `32` | `53` | Position_Unknown | Team_Unknown | 107–130 | 24 | 1 | Undefined position; Undefined team |
| `33` | `54` | Position_Unknown | Team_Unknown | 110–299 | 166 | 3 | Undefined position; Undefined team |
| `34` | `56` | Position_Unknown | Team_Unknown | 116–299 | 151 | 8 | Undefined position; Undefined team |
| `35` | `57` | Position_Unknown | Team_Unknown | 125–221 | 94 | 6 | Undefined position; Undefined team |
| `36` | `61` | Position_Unknown | Team_Unknown | 136–137 | 2 | 1 | Undefined position; Undefined team |
| `37` | `63` | Position_Unknown | Team_Unknown | 139–162 | 24 | 1 | Undefined position; Undefined team |
| `38` | `68` | Position_Unknown | Team_Unknown | 157–298 | 127 | 5 | Undefined position; Undefined team |
| `39` | `71` | Position_Unknown | Team_Unknown | 167–299 | 96 | 9 | Undefined position; Undefined team |
| `40` | `72` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `41` | `75` | Position_Unknown | Team_Unknown | 178–240 | 53 | 5 | Undefined position; Undefined team |
| `42` | `78` | Position_Unknown | Team_Unknown | 203–225 | 7 | 2 | Undefined position; Undefined team |
| `43` | `79` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |
| `44` | `80` | Position_Unknown | Team_Unknown | 209–211 | 3 | 1 | Undefined position; Undefined team |
| `45` | `82` | Position_Unknown | Team_Unknown | 213–263 | 13 | 5 | Undefined position; Undefined team |
| `46` | `86` | Position_Unknown | Team_Unknown | 218–243 | 17 | 5 | Undefined position; Undefined team |
| `47` | `89` | Position_Unknown | Team_Unknown | 220–225 | 6 | 1 | Undefined position; Undefined team |
| `48` | `90` | Position_Unknown | Team_Unknown | 221–294 | 50 | 2 | Undefined position; Undefined team |
| `49` | `93` | Position_Unknown | Team_Unknown | 222–247 | 25 | 2 | Undefined position; Undefined team |
| `50` | `95` | Position_Unknown | Team_Unknown | 226–299 | 74 | 1 | Undefined position; Undefined team |
| `51` | `96` | Position_Unknown | Team_Unknown | 235–236 | 2 | 1 | Undefined position; Undefined team |
| `52` | `97` | Position_Unknown | Team_Unknown | 243–245 | 3 | 1 | Undefined position; Undefined team |
| `53` | `98` | Position_Unknown | Team_Unknown | 248–290 | 32 | 3 | Undefined position; Undefined team |
| `54` | `101` | Position_Unknown | Team_Unknown | 255–289 | 24 | 4 | Undefined position; Undefined team |
| `55` | `102` | Position_Unknown | Team_Unknown | 270–299 | 25 | 4 | Undefined position; Undefined team |
| `56` | `103` | Position_Unknown | Team_Unknown | 274–295 | 22 | 1 | Undefined position; Undefined team |
| `57` | `104` | Position_Unknown | Team_Unknown | 278–299 | 19 | 2 | Undefined position; Undefined team |
| `58` | `105` | Position_Unknown | Team_Unknown | 280–299 | 17 | 2 | Undefined position; Undefined team |
| `59` | `106` | Position_Unknown | Team_Unknown | 281–283 | 3 | 1 | Undefined position; Undefined team |
| `60` | `107` | Position_Unknown | Team_Unknown | 293–299 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CatchPunt` and target `57` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `57` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ 51 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 51 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 102 |
| Missing visible bounding boxes during action | 197 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PuntBall' range [64-82] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-48] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-90] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-98] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-111] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-123] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-135] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-139] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-172] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-151] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-158] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-165] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-176] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-183] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-195] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-69] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-85] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-101] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-109] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-193] for track '3' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-215] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-225] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-242] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-282] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-52] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-31] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-67] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-110] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-113] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-108] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-133] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-158] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-127] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-139] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-30] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-32] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-14] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-25] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-9] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-40] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-96] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-108] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-9] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-154] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-157] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-181] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-97] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-134] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-140] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-151] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-157] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-33] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-61] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-66] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-130] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-59] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-83] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-102] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-57] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-75] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-100] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-81] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-66] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-119] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-130] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-230] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-75] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-96] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-103] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-171] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-183] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-194] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-246] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-270] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-282] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-285] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-116] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-130] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-153] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-141] for track '27' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-225] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-238] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-96] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-99] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-123] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-131] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-100] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-128] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-156] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-130] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-168] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-199] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-119] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-123] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-141] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-147] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-185] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-195] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-176] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchPunt' for track '35' starts at frame 177, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_CatchPunt' range [177-177] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [193-200] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [202-221] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-137] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-162] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-189] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-200] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-212] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-294] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-298] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-172] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-183] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-187] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-202] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-215] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-233] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-243] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-181] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-195] for track '41' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-198] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-225] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-240] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-205] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-225] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-210] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-211] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-215] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-220] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-240] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-256] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-263] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-219] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-228] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-238] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-243] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-225] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-268] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-294] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-238] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-247] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-245] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-264] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-282] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-290] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-259] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-265] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-276] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-289] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-276] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-287] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-291] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-295] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-291] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-290] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-283] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.

</details>