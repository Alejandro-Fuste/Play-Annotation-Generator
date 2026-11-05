# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_34

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_34`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 389
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 147
- **Validation Warnings:** 175
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 137
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `6` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `0` | `0` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `0` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `1` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `11` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `2` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `3` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `4` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `6` | `Group` | 0 | START | 0 | 51 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `6` | `6` | 52 | START | 52 | 108 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `0` | `0` | 79 | END | 79 | 79 |
| ✅ EXACT | `Action_PuntBall` | Punter | `0` | `0` | 109 | START | 109 | 389 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 85 | 34 | inferred_complete_timeline |
| `Action_None` | 87 | 112 | 26 | inferred_complete_timeline |
| `Action_None` | 119 | 121 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_LongSnap` | 52 | 108 | 57 | inferred_complete_timeline |
| `Action_None` | 109 | 249 | 141 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_None` | 262 | 296 | 35 | inferred_complete_timeline |
| `Action_None` | 301 | 389 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–317
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 252 | 201 | inferred_complete_timeline |
| `Action_None` | 256 | 317 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 126 | 75 | inferred_complete_timeline |
| `Action_None` | 130 | 379 | 250 | inferred_complete_timeline |
| `Action_None` | 387 | 389 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_SnapReceive` | 79 | 79 | 1 | inferred_complete_timeline |
| `Action_None` | 80 | 108 | 29 | inferred_complete_timeline |
| `Action_PuntBall` | 109 | 389 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 132 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 138 | 87 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–365
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 365 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 81 | 30 | inferred_complete_timeline |
| `Action_None` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_None` | 105 | 144 | 40 | inferred_complete_timeline |
| `Action_None` | 146 | 195 | 50 | inferred_complete_timeline |
| `Action_None` | 203 | 389 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 109 | 58 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_None` | 114 | 123 | 10 | inferred_complete_timeline |
| `Action_None` | 130 | 192 | 63 | inferred_complete_timeline |
| `Action_None` | 197 | 199 | 3 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |
| `Action_None` | 216 | 223 | 8 | inferred_complete_timeline |
| `Action_None` | 225 | 227 | 3 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 389 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–372
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 81 | 30 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_None` | 87 | 134 | 48 | inferred_complete_timeline |
| `Action_None` | 138 | 145 | 8 | inferred_complete_timeline |
| `Action_None` | 147 | 153 | 7 | inferred_complete_timeline |
| `Action_None` | 156 | 172 | 17 | inferred_complete_timeline |
| `Action_None` | 182 | 186 | 5 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 193 | 199 | 7 | inferred_complete_timeline |
| `Action_None` | 202 | 262 | 61 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |
| `Action_None` | 277 | 281 | 5 | inferred_complete_timeline |
| `Action_None` | 285 | 286 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 372 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 48 | 35 | inferred_complete_timeline |
| `Action_None` | 61 | 64 | 4 | inferred_complete_timeline |
| `Action_None` | 66 | 92 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–365
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 122 | 71 | inferred_complete_timeline |
| `Action_None` | 126 | 134 | 9 | inferred_complete_timeline |
| `Action_None` | 137 | 244 | 108 | inferred_complete_timeline |
| `Action_None` | 247 | 251 | 5 | inferred_complete_timeline |
| `Action_None` | 289 | 292 | 4 | inferred_complete_timeline |
| `Action_None` | 328 | 359 | 32 | inferred_complete_timeline |
| `Action_None` | 362 | 365 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_None` | 52 | 272 | 221 | inferred_complete_timeline |
| `Action_None` | 279 | 389 | 111 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–160 | 152 | 5 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 64–77 | 13 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 101–121 | 21 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 111–389 | 279 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 114–121 | 8 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 117–228 | 106 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 124–200 | 75 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 125–389 | 258 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 125–126 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 130–273 | 134 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 132–195 | 56 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 133–389 | 257 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 138–140 | 3 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 155–389 | 223 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 161–241 | 63 | 4 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 172–388 | 166 | 10 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 179–389 | 147 | 6 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 179–211 | 32 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 223–389 | 112 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 232–343 | 95 | 4 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 238–389 | 152 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 243–377 | 128 | 4 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 252–282 | 31 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 271–377 | 95 | 2 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 305–343 | 29 | 3 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 332–389 | 58 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 353–389 | 26 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 118 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [52-138] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-252] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-317] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-126] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-379] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-132] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-365] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-249] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-296] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-160] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-81] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-134] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-145] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-153] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-172] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-262] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-372] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-134] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-244] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-365] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-272] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-85] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-223] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-81] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-144] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-195] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-389] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-48] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-64] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-92] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-121] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-389] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-218] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-228] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-188] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-200] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-166] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-238] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-273] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-168] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-251] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-172] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-204] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-241] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-190] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-208] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-217] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-285] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-311] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-317] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-350] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-388] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-193] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-229] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-323] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-337] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-200] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-211] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-283] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-244] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-343] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-293] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-335] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-369] for track '35' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-377] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-282] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-377] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-313] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-337] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-343] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-362] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>