# Play-Annotation-Generator Annotation Review — BootPass_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_37`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_-`
- **Result Frame:** 299
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 126
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 103
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_RunFlatRoute` | RB2 | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_SecureCatch` | RB2 | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `2` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `6` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 25 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 26 | START | 26 | 40 |
| ✅ EXACT | `Action_RunBlock` | LT | `12` | `12` | 34 | START | 34 | 299 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `17` | `17` | 34 | START | 41 | 299 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `18` | `18` | 34 | START | 34 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `19` | `19` | 34 | START | 34 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `21` | `21` | 34 | START | 34 | 48 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 40 | END | 26 | 40 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `14` | `14` | 55 | START | 55 | 70 |
| ✅ EXACT | `Action_BootAway` | QB | `14` | `14` | 71 | START | 71 | 98 |
| ✅ EXACT | `Action_RunFlatRoute` | RB2 | `6` | `6` | 95 | START | 95 | 121 |
| ✅ EXACT | `Action_ThrowPass` | QB | `14` | `14` | 104 | START | 104 | 113 |
| ✅ EXACT | `Action_SecureCatch` | RB2 | `6` | `6` | 124 | START | 124 | 141 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 26 | 40 | 15 | inferred_complete_timeline |
| `Action_None` | 41 | 54 | 14 | inferred_complete_timeline |
| `Action_FakeHandoff` | 55 | 70 | 16 | inferred_complete_timeline |
| `Action_BootAway` | 71 | 98 | 28 | inferred_complete_timeline |
| `Action_None` | 99 | 103 | 5 | inferred_complete_timeline |
| `Action_ThrowPass` | 104 | 113 | 10 | inferred_complete_timeline |
| `Action_None` | 114 | 299 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 63 | 38 | inferred_complete_timeline |
| `Action_None` | 65 | 91 | 27 | inferred_complete_timeline |
| `Action_None` | 93 | 258 | 166 | inferred_complete_timeline |
| `Action_None` | 269 | 298 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 95 | 121 | 27 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_SecureCatch` | 124 | 141 | 18 | inferred_complete_timeline |
| `Action_None` | 142 | 244 | 103 | inferred_complete_timeline |
| `Action_None` | 247 | 250 | 4 | inferred_complete_timeline |
| `Action_None` | 252 | 255 | 4 | inferred_complete_timeline |
| `Action_None` | 257 | 299 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 208 | 183 | inferred_complete_timeline |
| `Action_None` | 212 | 299 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 161 | 136 | inferred_complete_timeline |
| `Action_None` | 163 | 186 | 24 | inferred_complete_timeline |
| `Action_None` | 188 | 224 | 37 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_None` | 241 | 244 | 4 | inferred_complete_timeline |
| `Action_None` | 247 | 257 | 11 | inferred_complete_timeline |
| `Action_None` | 260 | 299 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 236 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_RunBlock` | 34 | 299 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_RunBlock` | 34 | 41 | 8 | inferred_complete_timeline |
| `Action_RunBlock` | 43 | 48 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 53 | 113 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_BallSnap` | 26 | 40 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 41 | 299 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_RunBlock` | 34 | 48 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 53 | 156 | 104 | inferred_complete_timeline |
| `Action_RunBlock` | 158 | 247 | 90 | inferred_complete_timeline |
| `Action_RunBlock` | 255 | 258 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 260 | 278 | 19 | inferred_complete_timeline |
| `Action_RunBlock` | 280 | 287 | 8 | inferred_complete_timeline |
| `Action_RunBlock` | 290 | 291 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 293 | 297 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_RunBlock` | 34 | 86 | 53 | inferred_complete_timeline |
| `Action_RunBlock` | 90 | 299 | 210 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 54 | 29 | inferred_complete_timeline |
| `Action_None` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 107 | 29 | inferred_complete_timeline |
| `Action_None` | 113 | 132 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 53 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 139 | 114 | inferred_complete_timeline |
| `Action_None` | 149 | 294 | 146 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 179 | 154 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 281 | 90 | inferred_complete_timeline |
| `Action_None` | 284 | 299 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 140 | 115 | inferred_complete_timeline |
| `Action_None` | 145 | 149 | 5 | inferred_complete_timeline |
| `Action_None` | 160 | 258 | 99 | inferred_complete_timeline |
| `Action_None` | 268 | 270 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 212 | 187 | inferred_complete_timeline |
| `Action_None` | 221 | 299 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 88 | 63 | inferred_complete_timeline |
| `Action_None` | 94 | 260 | 167 | inferred_complete_timeline |
| `Action_None` | 263 | 265 | 3 | inferred_complete_timeline |
| `Action_None` | 268 | 271 | 4 | inferred_complete_timeline |
| `Action_None` | 277 | 278 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 284 | 259 | inferred_complete_timeline |
| `Action_None` | 292 | 299 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 178 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 223 | 198 | inferred_complete_timeline |
| `Action_None` | 229 | 233 | 5 | inferred_complete_timeline |
| `Action_None` | 240 | 242 | 3 | inferred_complete_timeline |
| `Action_None` | 249 | 260 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 163 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 53–299 | 246 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 69–81 | 6 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 109–110 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 123–299 | 177 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 131–299 | 169 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 139–211 | 69 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 186–211 | 26 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 196–254 | 52 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 200–212 | 5 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 207–221 | 11 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 208–211 | 4 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 273–275 | 3 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 277–293 | 16 | 2 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 281–285 | 5 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 282–296 | 11 | 3 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 284–299 | 16 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 294–299 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_RunBlock` for actor_track_id `17` (C): Annotated start 34 != Inferred start 41
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `21` (8 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [26–40], lower_priority='Action_RunBlock' annotated_start=34, effective_Action_RunBlock_start=41.
- ⚠️ Action 'Action_None' range [26-208] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-236] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-63] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-91] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-258] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-298] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-88] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-260] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-271] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-284] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-179] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-281] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-244] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-255] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-258] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-212] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-186] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-224] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-257] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-223] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-233] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-260] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-163] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-54] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [34-41] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [43-48] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [53-113] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [34-86] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [90-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-294] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [34-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [53-156] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [158-247] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [255-258] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [260-278] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [280-287] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [290-291] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [293-297] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-287] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-185] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-211] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-211] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-222] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-254] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-221] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-288] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-296] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '38' has 2 frames without a visible bounding box.
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

</details>