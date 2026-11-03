# Play-Annotation-Generator Annotation Review — PuntBlock_72

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_72`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 128
- **Validation Warnings:** 151
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 112
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `5` | `5` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `5` | `5` |
| ✅ EXACT | `Action_BlockPunt` | Position_Unknown | Team_Unknown | `17` | `17` |
| ✅ EXACT | `Action_SecureRecovery` | Personal_Protector1 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `0` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `15` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `2` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `3` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `5` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `8` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `9` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `14` | `14` | 16 | START | 16 | 66 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `5` | `5` | 41 | END | 41 | 41 |
| ✅ EXACT | `Action_PuntBall` | Punter | `5` | `5` | 67 | START | 67 | 83 |
| ✅ EXACT | `Action_BlockPunt` | Position_Unknown | `17` | `17` | 75 | START | 75 | 82 |
| ✅ EXACT | `Action_SecureRecovery` | Personal_Protector1 | `2` | `2` | 136 | START | 136 | 138 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–282
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 282 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 53 | 38 | inferred_complete_timeline |
| `Action_None` | 65 | 72 | 8 | inferred_complete_timeline |
| `Action_None` | 75 | 128 | 54 | inferred_complete_timeline |
| `Action_None` | 139 | 194 | 56 | inferred_complete_timeline |
| `Action_None` | 197 | 202 | 6 | inferred_complete_timeline |
| `Action_None` | 206 | 217 | 12 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_LongSnap` | 16 | 66 | 51 | inferred_complete_timeline |
| `Action_None` | 67 | 133 | 67 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 135 | 31 | inferred_complete_timeline |
| `Action_SecureRecovery` | 136 | 138 | 3 | inferred_complete_timeline |
| `Action_None` | 139 | 253 | 115 | inferred_complete_timeline |
| `Action_None` | 255 | 299 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 83 | 68 | inferred_complete_timeline |
| `Action_None` | 88 | 98 | 11 | inferred_complete_timeline |
| `Action_None` | 104 | 110 | 7 | inferred_complete_timeline |
| `Action_None` | 112 | 248 | 137 | inferred_complete_timeline |
| `Action_None` | 251 | 254 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 75 | 60 | inferred_complete_timeline |
| `Action_None` | 95 | 101 | 7 | inferred_complete_timeline |
| `Action_None` | 105 | 299 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_SnapReceive` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_None` | 42 | 66 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 67 | 83 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 66 | 51 | inferred_complete_timeline |
| `Action_None` | 68 | 187 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 68 | 53 | inferred_complete_timeline |
| `Action_None` | 71 | 134 | 64 | inferred_complete_timeline |
| `Action_None` | 150 | 189 | 40 | inferred_complete_timeline |
| `Action_None` | 192 | 221 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 50 | 35 | inferred_complete_timeline |
| `Action_None` | 58 | 104 | 47 | inferred_complete_timeline |
| `Action_None` | 118 | 182 | 65 | inferred_complete_timeline |
| `Action_None` | 196 | 231 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 32 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 62 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 36 | 21 | inferred_complete_timeline |
| `Action_None` | 50 | 168 | 119 | inferred_complete_timeline |
| `Action_None` | 172 | 218 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 64 | 49 | inferred_complete_timeline |
| `Action_None` | 95 | 116 | 22 | inferred_complete_timeline |
| `Action_None` | 118 | 123 | 6 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 194 | 60 | inferred_complete_timeline |
| `Action_None` | 198 | 252 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–28
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 28 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–28
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 28 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–279 | 272 | 7 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 2–239 | 214 | 7 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 20–56 | 29 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 30–75 | 46 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 43–45 | 3 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 47–210 | 158 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 55–242 | 181 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 55–72 | 17 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 64–257 | 181 | 6 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 70–81 | 4 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 76–234 | 150 | 6 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 93–127 | 35 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 100–101 | 2 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 115–122 | 8 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 122–290 | 163 | 3 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 123–299 | 176 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 126–231 | 106 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 141–187 | 18 | 5 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 151–234 | 84 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 164–205 | 35 | 2 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 214–244 | 31 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 269–299 | 31 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 291–299 | 9 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Jammer` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 101 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [16-53] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-72] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-194] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-217] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-50] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-104] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-182] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-231] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-253] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-282] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-36] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-168] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-218] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [67-83] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-196] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-219] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-274] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-279] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-28] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-66] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-68] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-134] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-189] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-64] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-116] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-194] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-252] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-32] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-83] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-98] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-110] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-248] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-62] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-28] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-8] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-14] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-136] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-239] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-46] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-45] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-55] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-178] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-95] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-110] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-153] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-242] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-69] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-77] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-104] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-206] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-257] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-93] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-107] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-145] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-194] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-234] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-127] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-122] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-164] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-290] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-249] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-299] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-231] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-173] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-234] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-195] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-244] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-299] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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

</details>