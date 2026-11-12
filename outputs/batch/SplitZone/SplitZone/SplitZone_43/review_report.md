# Play-Annotation-Generator Annotation Review — SplitZone_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_43`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 121
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 102
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_BlockSecondLevel` | WR3 | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `19` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `12` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 6 | 10 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 74 | START | 74 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `13` | `13` | 77 | START | 77 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `14` | `14` | 77 | START | 77 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `17` | 77 | START | 90 | 91 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `20` | 77 | START | 77 | 115 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `21` | `21` | 77 | START | N/A | N/A |
| ✅ EXACT | `Action_SplitBlock` | TE | `11` | `11` | 81 | START | 81 | 115 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 89 | END | 74 | 89 |
| ✅ EXACT | `Action_BlockSecondLevel` | WR3 | `12` | `12` | 91 | START | 91 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `19` | `19` | 113 | START | 113 | 302 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 115 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–308
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SnapReceive` | 74 | 89 | 16 | inferred_complete_timeline |
| `Action_None` | 90 | 98 | 9 | inferred_complete_timeline |
| `Action_None` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_None` | 107 | 112 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 113 | 302 | 190 | inferred_complete_timeline |
| `Action_BallCarry` | 307 | 308 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 177 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 167 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 329 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 91 | 115 | 25 | inferred_complete_timeline |
| `Action_None` | 116 | 123 | 8 | inferred_complete_timeline |
| `Action_None` | 183 | 195 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_SplitBlock` | 81 | 115 | 35 | inferred_complete_timeline |
| `Action_None` | 116 | 329 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 105 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 115 | 9 | inferred_complete_timeline |
| `Action_None` | 116 | 164 | 49 | inferred_complete_timeline |
| `Action_None` | 169 | 302 | 134 | inferred_complete_timeline |
| `Action_None` | 304 | 316 | 13 | inferred_complete_timeline |
| `Action_None` | 321 | 329 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 6–23
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 10 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 23 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_BallSnap` | 74 | 89 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 113 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 115 | 1 | inferred_complete_timeline |
| `Action_None` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 148 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 88 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 115 | 25 | inferred_complete_timeline |
| `Action_None` | 116 | 138 | 23 | inferred_complete_timeline |
| `Action_None` | 141 | 329 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 115 | 39 | inferred_complete_timeline |
| `Action_None` | 116 | 210 | 95 | inferred_complete_timeline |
| `Action_None` | 213 | 216 | 4 | inferred_complete_timeline |
| `Action_None` | 221 | 231 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 157 | 84 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 171 | 199 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 102 | 29 | inferred_complete_timeline |
| `Action_None` | 111 | 322 | 212 | inferred_complete_timeline |
| `Action_None` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 129 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 100 | 27 | inferred_complete_timeline |
| `Action_None` | 129 | 135 | 7 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 166 | 7 | inferred_complete_timeline |
| `Action_None` | 174 | 187 | 14 | inferred_complete_timeline |
| `Action_None` | 189 | 261 | 73 | inferred_complete_timeline |
| `Action_None` | 264 | 265 | 2 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 329 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 217 | 144 | inferred_complete_timeline |
| `Action_None` | 222 | 291 | 70 | inferred_complete_timeline |
| `Action_None` | 294 | 298 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 329 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 329 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 295 | 222 | inferred_complete_timeline |
| `Action_None` | 298 | 314 | 17 | inferred_complete_timeline |
| `Action_None` | 321 | 326 | 6 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 259 | 186 | inferred_complete_timeline |
| `Action_None` | 265 | 284 | 20 | inferred_complete_timeline |
| `Action_None` | 287 | 326 | 40 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 148 | 75 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 80–94 | 12 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 109–329 | 216 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 146–329 | 174 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 165–236 | 13 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 176–329 | 154 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 177–329 | 153 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 183–209 | 15 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 184–290 | 107 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 205–303 | 82 | 5 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 208–210 | 3 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 217–224 | 8 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 223–311 | 68 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 224–329 | 106 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 230–329 | 99 | 2 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 244–246 | 3 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 260–329 | 26 | 4 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 274–329 | 56 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 288–289 | 2 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 304–329 | 26 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 327–329 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `21` (LG)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [74–89], lower_priority='Action_ZoneBlock' annotated_start=77, effective_Action_ZoneBlock_start=90.
- ⚠️ Segment 'Action_ZoneBlock' for track '21' has invalid range: start=77, end=23. Clamping end to start.
- ⚠️ Action 'Action_None' range [74-167] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-217] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-291] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-298] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-259] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-284] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-326] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-295] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-314] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-326] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-157] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-199] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-195] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-105] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-302] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-316] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-88] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-138] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-322] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [74-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-148] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-166] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-261] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-98] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [113-302] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [307-308] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-231] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-10] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-23] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-94] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-329] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-189] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-290] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-231] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-303] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-224] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-311] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-329] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-253] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-297] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-329] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '39' has 1 frames without a visible bounding box.
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