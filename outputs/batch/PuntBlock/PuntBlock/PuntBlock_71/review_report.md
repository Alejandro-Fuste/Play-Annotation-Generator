# Play-Annotation-Generator Annotation Review — PuntBlock_71

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_71`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 151
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `15` | `15` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `4` | `4` |
| ❌ MISSING SEGMENT | `Action_BlockPunt` | Interior_Rusher2 | defense | `9` | `9` |
| ✅ EXACT | `Action_SecureRecovery` | Punter | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `11` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `12` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `14` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `15` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `17` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `18` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `4` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `5` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `7` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `8` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `15` | `15` | 12 | START | 12 | 59 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `4` | `4` | 41 | END | 41 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `4` | `4` | 60 | START | 60 | 104 |
| ❌ MISSING SEGMENT | `Action_BlockPunt` | Interior_Rusher2 | `9` | `9` | 75 | START | N/A | N/A |
| ✅ EXACT | `Action_SecureRecovery` | Punter | `4` | `4` | 134 | START | 134 | 148 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–276
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 276 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 117 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 42 | 31 | inferred_complete_timeline |
| `Action_None` | 45 | 127 | 83 | inferred_complete_timeline |
| `Action_None` | 129 | 259 | 131 | inferred_complete_timeline |
| `Action_None` | 261 | 268 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_LongSnap` | 12 | 59 | 48 | inferred_complete_timeline |
| `Action_None` | 60 | 250 | 191 | inferred_complete_timeline |
| `Action_None` | 252 | 278 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 65 | 54 | inferred_complete_timeline |
| `Action_None` | 67 | 299 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 67 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 62 | 51 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_SnapReceive` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_None` | 42 | 59 | 18 | inferred_complete_timeline |
| `Action_PuntBall` | 60 | 104 | 45 | inferred_complete_timeline |
| `Action_PuntBall` | 106 | 133 | 28 | inferred_complete_timeline |
| `Action_SecureRecovery` | 134 | 148 | 15 | inferred_complete_timeline |
| `Action_None` | 149 | 258 | 110 | inferred_complete_timeline |
| `Action_None` | 261 | 275 | 15 | inferred_complete_timeline |
| `Action_None` | 279 | 283 | 5 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 49 | 38 | inferred_complete_timeline |
| `Action_None` | 110 | 269 | 160 | inferred_complete_timeline |
| `Action_None` | 281 | 299 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 208 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 275 | 264 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 64 | 53 | inferred_complete_timeline |
| `Action_None` | 66 | 191 | 126 | inferred_complete_timeline |
| `Action_None` | 201 | 238 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–67
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 67 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 122 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 42 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 86 | 75 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 205 | 102 | inferred_complete_timeline |
| `Action_None` | 208 | 218 | 11 | inferred_complete_timeline |
| `Action_None` | 222 | 249 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 71 | 60 | inferred_complete_timeline |
| `Action_None` | 75 | 80 | 6 | inferred_complete_timeline |
| `Action_None` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_None` | 97 | 101 | 5 | inferred_complete_timeline |
| `Action_None` | 103 | 107 | 5 | inferred_complete_timeline |
| `Action_None` | 117 | 221 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 120 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 146 | 135 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 24–73 | 49 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 36–285 | 232 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 38–299 | 259 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 40–149 | 110 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 67–90 | 19 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 76–109 | 34 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 93–121 | 29 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 94–104 | 9 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 112–113 | 2 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 117–299 | 155 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 120–121 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 127–273 | 147 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 128–154 | 6 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 128–299 | 157 | 5 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 163–253 | 90 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 175–220 | 45 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 216–255 | 33 | 4 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 250–259 | 4 | 2 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 265–273 | 8 | 2 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 271–299 | 20 | 4 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 278–299 | 22 | 1 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 285–297 | 7 | 2 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 285–297 | 5 | 2 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 287–295 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `4` (2 segments found)
- ❌ Missing segment for action `Action_BlockPunt` on target `9` (Interior_Rusher2)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Tackle` position mapped to `offense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 98 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_BlockPunt' for track '9' has invalid range: start=75, end=67. Clamping end to start.
- ⚠️ Action 'Action_None' range [12-117] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-71] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-80] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-107] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-221] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-86] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-205] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-218] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-249] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [60-104] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [106-133] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-258] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-275] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-283] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-62] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-88] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-42] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-42] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-127] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-259] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-268] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-49] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-67] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-64] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-191] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-238] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-65] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-276] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-146] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-208] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [12-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-250] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-278] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-122] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-67] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-275] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-31] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-73] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-152] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-253] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-285] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-198] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-212] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-258] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-299] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-149] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-78] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-84] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-109] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-121] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-125] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-299] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-273] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-131] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-238] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-257] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-267] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-253] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-205] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-220] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-223] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-255] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-290] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-289] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-295] for track '43' has 1 frames without a visible bounding box.
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

</details>