# Play-Annotation-Generator Annotation Review — Counter_36

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_36`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 48
- **Ball Tracks:** 0
- **Action Segments:** 131
- **Validation Warnings:** 155
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | TE1 | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | offense | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | SAF1 | defense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `10` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 73 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 74 | START | 74 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `13` | `12` | 77 | START | 77 | 124 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `14` | `13` | 77 | START | 86 | 176 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | TE1 | `8` | `7` | 77 | START | 77 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | `1` | `0` | 77 | START | 77 | 120 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 85 | END | 74 | 85 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `16` | 95 | START | 95 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | SAF1 | `3` | `2` | 128 | START | 128 | 313 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 180 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SnapReceive` | 74 | 85 | 12 | inferred_complete_timeline |
| `Action_None` | 86 | 94 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 95 | 127 | 33 | inferred_complete_timeline |
| `Action_None` | 128 | 138 | 11 | inferred_complete_timeline |
| `Action_None` | 147 | 190 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 177 | 104 | inferred_complete_timeline |
| `Action_None` | 179 | 182 | 4 | inferred_complete_timeline |
| `Action_None` | 191 | 225 | 35 | inferred_complete_timeline |
| `Action_None` | 233 | 329 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 90 | 17 | inferred_complete_timeline |
| `Action_None` | 99 | 128 | 30 | inferred_complete_timeline |
| `Action_None` | 130 | 205 | 76 | inferred_complete_timeline |
| `Action_None` | 208 | 244 | 37 | inferred_complete_timeline |
| `Action_None` | 246 | 319 | 74 | inferred_complete_timeline |
| `Action_None` | 321 | 322 | 2 | inferred_complete_timeline |
| `Action_None` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_PullBlock` | 77 | 102 | 26 | inferred_complete_timeline |
| `Action_PullBlock` | 104 | 180 | 77 | inferred_complete_timeline |
| `Action_None` | 181 | 329 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–303
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 77 | 120 | 44 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 123 | 180 | 58 | inferred_complete_timeline |
| `Action_None` | 181 | 238 | 58 | inferred_complete_timeline |
| `Action_None` | 241 | 303 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–321
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 137 | 64 | inferred_complete_timeline |
| `Action_None` | 139 | 198 | 60 | inferred_complete_timeline |
| `Action_None` | 217 | 219 | 3 | inferred_complete_timeline |
| `Action_None` | 234 | 237 | 4 | inferred_complete_timeline |
| `Action_None` | 239 | 241 | 3 | inferred_complete_timeline |
| `Action_None` | 243 | 321 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 111 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_BallSnap` | 74 | 85 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 86 | 176 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_DownBlock` | 77 | 124 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 126 | 129 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 145 | 180 | 36 | inferred_complete_timeline |
| `Action_None` | 181 | 329 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 131 | 58 | inferred_complete_timeline |
| `Action_None` | 138 | 161 | 24 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 188 | 115 | inferred_complete_timeline |
| `Action_None` | 190 | 329 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 86 | 13 | inferred_complete_timeline |
| `Action_None` | 117 | 122 | 6 | inferred_complete_timeline |
| `Action_None` | 124 | 128 | 5 | inferred_complete_timeline |
| `Action_None` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 159 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 73 | 36 | inferred_complete_timeline |
| `Action_None` | 74 | 77 | 4 | inferred_complete_timeline |
| `Action_None` | 112 | 127 | 16 | inferred_complete_timeline |
| `Action_None` | 129 | 205 | 77 | inferred_complete_timeline |
| `Action_None` | 215 | 329 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–27
- **Visible Samples:** 15

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 27 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 100 | 27 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–322
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 129 | 56 | inferred_complete_timeline |
| `Action_None` | 140 | 190 | 51 | inferred_complete_timeline |
| `Action_None` | 201 | 322 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–18
- **Visible Samples:** 19

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 139 | 66 | inferred_complete_timeline |
| `Action_None` | 144 | 293 | 150 | inferred_complete_timeline |
| `Action_None` | 301 | 329 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_BallCarry` | 128 | 313 | 186 | inferred_complete_timeline |
| `Action_BallCarry` | 319 | 329 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 184 | 111 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 85–156 | 62 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 92–97 | 6 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 95–172 | 73 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 112–114 | 3 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 136–255 | 111 | 4 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 175–192 | 16 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 204–318 | 115 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 218–229 | 12 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 226–329 | 104 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 231–246 | 16 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 249–266 | 17 | 2 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 252–313 | 62 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 253–329 | 77 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 263–308 | 38 | 3 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 264–322 | 55 | 2 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 264–309 | 23 | 3 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 272–277 | 6 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 272–329 | 58 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 272–274 | 3 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 275–329 | 19 | 3 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 281–304 | 24 | 1 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 293–329 | 37 | 1 | Undefined position; Undefined team |
| `43` | `59` | Position_Unknown | Team_Unknown | 296–329 | 34 | 1 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 314–329 | 8 | 2 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 320–329 | 10 | 1 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 320–329 | 10 | 1 | Undefined position; Undefined team |
| `47` | `63` | Position_Unknown | Team_Unknown | 324–329 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (4 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `14` (C): Annotated start 77 != Inferred start 86
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 94 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '7' (TE1) duration 104 frames exceeds threshold 90 frames [start=77, end=180].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (RG) duration 104 frames exceeds threshold 90 frames [start=77, end=180].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (C) duration 100 frames exceeds threshold 90 frames [start=77, end=176].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [74–85], lower_priority='Action_DownBlock' annotated_start=77, effective_Action_DownBlock_start=86.
- ⚠️ Action 'Action_PullLeadBlock' range [77-120] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-238] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-303] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [128-313] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-293] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-198] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-321] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-177] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-225] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-329] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-188] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-329] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [77-102] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-111] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-90] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-128] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-205] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-244] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-319] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-131] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-161] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [77-124] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [126-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [145-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [86-176] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-129] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-190] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-322] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-122] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-159] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-190] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-184] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-27] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-127] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-205] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-116] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-156] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-168] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-236] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-251] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-192] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-318] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-229] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-246] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-261] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-313] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-329] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-276] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-303] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-314] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-322] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-277] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-286] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-277] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-279] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-322] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-304] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-319] for track '44' has 1 frames without a visible bounding box.
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

</details>