# Play-Annotation-Generator Annotation Review — PuntBlock_40

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_40`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 120
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `0` | `0` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `0` | `0` |
| ✅ EXACT | `Action_BlockPunt` | Right_Tackle | offense | `2` | `2` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Right_Tackle | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `0` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `11` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `2` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `3` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `4` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `5` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `6` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `7` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `9` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `5` | `5` | 1 | START | 1 | 53 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `0` | `0` | 31 | END | 31 | 31 |
| ✅ EXACT | `Action_PuntBall` | Punter | `0` | `0` | 54 | START | 54 | 154 |
| ✅ EXACT | `Action_BlockPunt` | Right_Tackle | `2` | `2` | 67 | START | 67 | 75 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Right_Tackle | `2` | `2` | 199 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 221 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 172 | 172 | inferred_complete_timeline |
| `Action_None` | 182 | 194 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 236 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 81 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_LongSnap` | 1 | 53 | 53 | inferred_complete_timeline |
| `Action_None` | 54 | 241 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 298 | 298 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 172 | 172 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 31 | 1 | inferred_complete_timeline |
| `Action_None` | 32 | 53 | 22 | inferred_complete_timeline |
| `Action_PuntBall` | 54 | 154 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 45 | 45 | inferred_complete_timeline |
| `Action_None` | 47 | 220 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_BlockPunt` | 67 | 75 | 9 | inferred_complete_timeline |
| `Action_None` | 76 | 133 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 72 | 72 | inferred_complete_timeline |
| `Action_None` | 79 | 156 | 78 | inferred_complete_timeline |
| `Action_None` | 158 | 188 | 31 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 14 | 14 | inferred_complete_timeline |
| `Action_None` | 16 | 18 | 3 | inferred_complete_timeline |
| `Action_None` | 22 | 23 | 2 | inferred_complete_timeline |
| `Action_None` | 25 | 26 | 2 | inferred_complete_timeline |
| `Action_None` | 32 | 39 | 8 | inferred_complete_timeline |
| `Action_None` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_None` | 55 | 220 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 134 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 23 | 23 | inferred_complete_timeline |
| `Action_None` | 25 | 35 | 11 | inferred_complete_timeline |
| `Action_None` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_None` | 44 | 126 | 83 | inferred_complete_timeline |
| `Action_None` | 130 | 138 | 9 | inferred_complete_timeline |
| `Action_None` | 143 | 245 | 103 | inferred_complete_timeline |
| `Action_None` | 249 | 251 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 20 | 20 | inferred_complete_timeline |
| `Action_None` | 33 | 299 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–30
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 23 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 30 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 170 | 170 | inferred_complete_timeline |
| `Action_None` | 172 | 183 | 12 | inferred_complete_timeline |
| `Action_None` | 188 | 195 | 8 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 219 | 4 | inferred_complete_timeline |
| `Action_None` | 241 | 299 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 3–73 | 71 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 21–187 | 159 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 46–52 | 7 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 77–88 | 12 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 92–290 | 199 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 96–222 | 127 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 101–154 | 33 | 6 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 102–120 | 19 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 112–296 | 134 | 6 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 119–130 | 11 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 144–216 | 73 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 146–257 | 80 | 5 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 146–200 | 38 | 4 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 162–299 | 137 | 2 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 174–175 | 2 | 1 | Undefined position; Undefined team |
| `34` | `36` | Position_Unknown | Team_Unknown | 174–175 | 2 | 1 | Undefined position; Undefined team |
| `35` | `37` | Position_Unknown | Team_Unknown | 228–236 | 9 | 1 | Undefined position; Undefined team |
| `36` | `38` | Position_Unknown | Team_Unknown | 268–299 | 32 | 1 | Undefined position; Undefined team |
| `37` | `39` | Position_Unknown | Team_Unknown | 285–291 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SecureRecovery` on target `2` (Right_Tackle)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureRecovery' for track '2' has invalid range: start=199, end=133. Clamping end to start.
- ⚠️ Action 'Action_PuntBall' range [54-154] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-133] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-298] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-45] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-220] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-241] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-236] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-81] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-72] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-156] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-188] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-172] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-194] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-23] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-30] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-172] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-134] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-14] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-18] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-23] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-26] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-39] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-47] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-220] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-170] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-195] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-219] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-23] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-35] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-126] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-245] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-20] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-73] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-172] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-52] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-290] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-222] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-111] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-117] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-130] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-229] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-296] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-130] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-216] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-201] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-211] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-222] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-159] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-189] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-175] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-236] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '37' has 1 frames without a visible bounding box.
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

</details>