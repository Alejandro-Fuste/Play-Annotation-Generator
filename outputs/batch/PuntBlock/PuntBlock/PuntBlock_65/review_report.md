# Play-Annotation-Generator Annotation Review — PuntBlock_65

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_65`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 1
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `18` | `18` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_BlockPunt` | Right_Edge_Rusher1 | defense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Right_Tackle | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | `0` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `1` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `10` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `13` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `14` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `18` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `19` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `4` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | `6` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `7` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `9` | `Group` | 0 | START | 0 | 7 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `18` | `18` | 8 | START | 8 | 37 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `14` | `14` | 35 | END | 35 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `14` | `14` | 60 | START | 60 | 80 |
| ❌ MISSING SEGMENT | `Action_BlockPunt` | Right_Edge_Rusher1 | `11` | `11` | 74 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureRecovery` | Right_Tackle | `7` | `7` | 155 | START | 155 | 162 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 55 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 224 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 268 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 329 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_LongSnap` | 8 | 37 | 30 | inferred_complete_timeline |
| `Action_LongSnap` | 39 | 59 | 21 | inferred_complete_timeline |
| `Action_None` | 60 | 99 | 40 | inferred_complete_timeline |
| `Action_None` | 103 | 109 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 329 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 63 | 56 | inferred_complete_timeline |
| `Action_None` | 68 | 134 | 67 | inferred_complete_timeline |
| `Action_None` | 137 | 199 | 63 | inferred_complete_timeline |
| `Action_None` | 207 | 211 | 5 | inferred_complete_timeline |
| `Action_None` | 213 | 329 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_SnapReceive` | 35 | 35 | 1 | inferred_complete_timeline |
| `Action_None` | 36 | 59 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 60 | 80 | 21 | inferred_complete_timeline |
| `Action_PuntBall` | 85 | 117 | 33 | inferred_complete_timeline |
| `Action_PuntBall` | 120 | 203 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 329 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 137 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_SecureRecovery` | 155 | 162 | 8 | inferred_complete_timeline |
| `Action_SecureRecovery` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_None` | 167 | 329 | 163 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 40 | 33 | inferred_complete_timeline |
| `Action_None` | 45 | 107 | 63 | inferred_complete_timeline |
| `Action_None` | 109 | 171 | 63 | inferred_complete_timeline |
| `Action_None` | 173 | 186 | 14 | inferred_complete_timeline |
| `Action_None` | 192 | 254 | 63 | inferred_complete_timeline |
| `Action_None` | 257 | 295 | 39 | inferred_complete_timeline |
| `Action_None` | 297 | 304 | 8 | inferred_complete_timeline |
| `Action_None` | 306 | 329 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 74 | 67 | inferred_complete_timeline |
| `Action_None` | 78 | 98 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 32 | 25 | inferred_complete_timeline |
| `Action_None` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_None` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_None` | 57 | 93 | 37 | inferred_complete_timeline |
| `Action_None` | 99 | 101 | 3 | inferred_complete_timeline |
| `Action_None` | 109 | 121 | 13 | inferred_complete_timeline |
| `Action_None` | 123 | 160 | 38 | inferred_complete_timeline |
| `Action_None` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_None` | 168 | 329 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 323 | 316 | inferred_complete_timeline |
| `Action_None` | 326 | 329 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 54 | 47 | inferred_complete_timeline |
| `Action_None` | 65 | 329 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 213 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 45 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 199 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 137 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 37–208 | 172 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 63–65 | 3 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 85–137 | 53 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 85–242 | 156 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 104–329 | 222 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 113–270 | 91 | 8 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 122–124 | 3 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 124–329 | 206 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 125–127 | 3 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 128–203 | 71 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 128–232 | 74 | 5 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 148–175 | 28 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 161–208 | 29 | 3 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 189–329 | 105 | 9 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 189–329 | 115 | 4 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 210–254 | 6 | 2 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 212–215 | 4 | 1 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 217–221 | 4 | 2 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 272–329 | 56 | 2 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 294–295 | 2 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 313–314 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PuntBall` and target `14` (3 segments found)
- ❌ Missing segment for action `Action_BlockPunt` on target `11` (Right_Edge_Rusher1)
- ⚠️ Ambiguous match for action `Action_SecureRecovery` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_BlockPunt' for track '11' has invalid range: start=74, end=35. Clamping end to start.
- ⚠️ Action 'Action_None' range [8-268] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-137] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-137] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-32] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-35] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-93] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-160] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-63] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-134] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-199] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-211] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-329] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-224] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-154] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureRecovery' range [155-162] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-54] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-55] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-213] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [60-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [85-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [120-203] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-323] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-40] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-186] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-254] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-295] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-304] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [8-37] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-99] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-109] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-74] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-98] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-208] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-65] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-137] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-242] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-249] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-133] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-147] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-162] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-177] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-244] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-270] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-182] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-203] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-149] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-222] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-175] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-169] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-208] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-216] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-232] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-242] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-252] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-300] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-317] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-198] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-264] for track '35' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-279] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-213] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-320] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '41' has 1 frames without a visible bounding box.
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

</details>