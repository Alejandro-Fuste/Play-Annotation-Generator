# Play-Annotation-Generator Annotation Review — SplitZone_121

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_121`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `5` | `5` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `18` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 25 | START | 26 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 25 | START | 26 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 25 | START | 26 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 25 | START | 26 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 25 | START | 26 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 25 | START | 26 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 25 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 25 | START | 26 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 25 | START | 26 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 25 | START | 26 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 25 | START | 26 | 111 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 112 | START | 112 | 128 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `10` | 115 | START | 115 | 242 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `18` | 115 | START | 129 | 135 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `19` | `19` | 115 | START | 115 | 242 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 115 | START | 119 | 202 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `7` | 115 | START | 115 | 217 |
| ✅ EXACT | `Action_SplitBlock` | TE | `6` | `6` | 118 | START | 118 | 135 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 128 | END | 112 | 128 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 137 | START | 137 | 142 |
| ✅ EXACT | `Action_BallCarry` | RB | `5` | `5` | 143 | START | 143 | 259 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `18` | `18` | 143 | START | 143 | 145 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 242 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 26–285
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_SnapReceive` | 112 | 128 | 17 | inferred_complete_timeline |
| `Action_None` | 129 | 136 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 137 | 142 | 6 | inferred_complete_timeline |
| `Action_None` | 143 | 196 | 54 | inferred_complete_timeline |
| `Action_None` | 204 | 240 | 37 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |
| `Action_None` | 254 | 260 | 7 | inferred_complete_timeline |
| `Action_None` | 265 | 285 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 26–259
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 142 | 117 | inferred_complete_timeline |
| `Action_BallCarry` | 143 | 259 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 26–326
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_None` | 112 | 309 | 198 | inferred_complete_timeline |
| `Action_None` | 318 | 326 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 26–264
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_None` | 112 | 264 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 26–359
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_None` | 112 | 359 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 26–135
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 117 | 92 | inferred_complete_timeline |
| `Action_SplitBlock` | 118 | 135 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 26–217
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 114 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 217 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 26–342
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 114 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 242 | 128 | inferred_complete_timeline |
| `Action_None` | 243 | 342 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 26–145
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_BallSnap` | 112 | 128 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 135 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 142 | 4 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 143 | 145 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 119–298
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 119 | 202 | 84 | inferred_complete_timeline |
| `Action_ZoneBlock` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 242 | 23 | inferred_complete_timeline |
| `Action_None` | 243 | 298 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 26–359
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 114 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 242 | 128 | inferred_complete_timeline |
| `Action_None` | 243 | 324 | 82 | inferred_complete_timeline |
| `Action_None` | 331 | 359 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 26–149
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_None` | 112 | 149 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 26–359
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_None` | 112 | 359 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 26–281
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_None` | 112 | 147 | 36 | inferred_complete_timeline |
| `Action_None` | 149 | 162 | 14 | inferred_complete_timeline |
| `Action_None` | 164 | 281 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 26–196
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_None` | 112 | 169 | 58 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 26–344
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_None` | 112 | 344 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 26–291
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_None` | 112 | 183 | 72 | inferred_complete_timeline |
| `Action_None` | 193 | 291 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 26–359
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_None` | 112 | 288 | 177 | inferred_complete_timeline |
| `Action_None` | 331 | 353 | 23 | inferred_complete_timeline |
| `Action_None` | 358 | 359 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 26–282
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_None` | 112 | 279 | 168 | inferred_complete_timeline |
| `Action_None` | 281 | 282 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 26–359
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_None` | 112 | 311 | 200 | inferred_complete_timeline |
| `Action_None` | 314 | 355 | 42 | inferred_complete_timeline |
| `Action_None` | 359 | 359 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 26–262
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_None` | 112 | 213 | 102 | inferred_complete_timeline |
| `Action_None` | 241 | 262 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 26–275
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_None` | 112 | 254 | 143 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |
| `Action_None` | 272 | 275 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 137–237 | 99 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 159–359 | 111 | 4 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 170–182 | 11 | 2 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 176–347 | 155 | 2 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 179–324 | 146 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 203–352 | 143 | 4 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 210–291 | 46 | 3 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 252–359 | 97 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 256–359 | 85 | 5 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 263–264 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 269–326 | 58 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 278–359 | 79 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 290–359 | 59 | 4 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 291–292 | 2 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 321–346 | 25 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 342–359 | 18 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 103 frames exceeds threshold 90 frames [start=115, end=217].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 128 frames exceeds threshold 90 frames [start=115, end=242].
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [112–128], lower_priority='Action_ZoneBlock' annotated_start=115, effective_Action_ZoneBlock_start=129.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LG) duration 128 frames exceeds threshold 90 frames [start=115, end=242].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 124 frames exceeds threshold 90 frames [start=119, end=242].
- ⚠️ Action 'Action_None' range [112-359] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-264] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-309] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-326] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-288] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-353] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-311] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-355] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [143-259] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [118-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-217] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-359] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-196] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-240] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-260] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-285] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-324] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-279] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-162] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-281] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-213] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-262] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-254] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-169] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-183] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-291] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-344] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [143-145] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-242] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-342] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-149] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [119-202] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [204-205] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [220-242] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-298] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-192] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-237] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-216] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-342] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-182] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-347] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-324] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-326] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-334] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-352] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-274] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-291] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-293] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-342] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-325] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-326] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-353] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-306] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-319] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-327] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-346] for track '36' has 1 frames without a visible bounding box.
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