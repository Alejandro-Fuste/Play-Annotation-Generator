# Play-Annotation-Generator Annotation Review — SplitZone_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_25`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 147
- **Validation Warnings:** 161
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 126
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_SplitBlock` | DT1 | defense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `20` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 4 | START | 4 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `1` | `Group` | 4 | START | 4 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 4 | START | 4 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 4 | START | 4 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 4 | START | 4 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 4 | START | 4 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 4 | START | 4 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 4 | START | 4 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 4 | START | 4 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 4 | START | 4 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 4 | START | 4 | 98 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 99 | START | 99 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `14` | `14` | 102 | START | 102 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `16` | 102 | START | 117 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `17` | 102 | START | 102 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `18` | 102 | START | 102 | 118 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 102 | START | 102 | 194 |
| ✅ EXACT | `Action_SplitBlock` | DT1 | `11` | `11` | 105 | START | 105 | 129 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 116 | END | 99 | 116 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `13` | 124 | START | 124 | 154 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `20` | `20` | 155 | START | 179 | 182 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 203 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 4–228
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 98 | 95 | inferred_complete_timeline |
| `Action_SnapReceive` | 99 | 116 | 18 | inferred_complete_timeline |
| `Action_None` | 117 | 123 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 124 | 154 | 31 | inferred_complete_timeline |
| `Action_None` | 155 | 228 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 4–182
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 146 | 143 | inferred_complete_timeline |
| `Action_BallCarry` | 179 | 182 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 4–158
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 98 | 95 | inferred_complete_timeline |
| `Action_None` | 99 | 144 | 46 | inferred_complete_timeline |
| `Action_None` | 156 | 158 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 4–340
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 98 | 95 | inferred_complete_timeline |
| `Action_None` | 99 | 340 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 4–339
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 98 | 95 | inferred_complete_timeline |
| `Action_None` | 99 | 293 | 195 | inferred_complete_timeline |
| `Action_None` | 314 | 318 | 5 | inferred_complete_timeline |
| `Action_None` | 327 | 330 | 4 | inferred_complete_timeline |
| `Action_None` | 332 | 339 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 4–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 98 | 95 | inferred_complete_timeline |
| `Action_None` | 99 | 359 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 4–359
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 101 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 118 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 129 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 131 | 135 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 146 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 175 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 203 | 27 | inferred_complete_timeline |
| `Action_None` | 204 | 293 | 90 | inferred_complete_timeline |
| `Action_None` | 295 | 359 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 4–129
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 101 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 112 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 129 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 4–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 98 | 95 | inferred_complete_timeline |
| `Action_BallSnap` | 99 | 116 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 129 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 131 | 161 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 183 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 203 | 18 | inferred_complete_timeline |
| `Action_None` | 204 | 359 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 4–359
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 101 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 151 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 194 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 197 | 203 | 7 | inferred_complete_timeline |
| `Action_None` | 204 | 359 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 4–194
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 101 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 194 | 93 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 4–144
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 6 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 98 | 78 | inferred_complete_timeline |
| `Action_None` | 99 | 129 | 31 | inferred_complete_timeline |
| `Action_None` | 131 | 135 | 5 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 4–355
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 98 | 95 | inferred_complete_timeline |
| `Action_None` | 99 | 133 | 35 | inferred_complete_timeline |
| `Action_None` | 140 | 144 | 5 | inferred_complete_timeline |
| `Action_None` | 177 | 182 | 6 | inferred_complete_timeline |
| `Action_None` | 185 | 346 | 162 | inferred_complete_timeline |
| `Action_None` | 350 | 351 | 2 | inferred_complete_timeline |
| `Action_None` | 354 | 355 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 4–129
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 104 | 101 | inferred_complete_timeline |
| `Action_SplitBlock` | 105 | 129 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 4–359
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 98 | 95 | inferred_complete_timeline |
| `Action_None` | 99 | 112 | 14 | inferred_complete_timeline |
| `Action_None` | 114 | 122 | 9 | inferred_complete_timeline |
| `Action_None` | 126 | 133 | 8 | inferred_complete_timeline |
| `Action_None` | 137 | 151 | 15 | inferred_complete_timeline |
| `Action_None` | 153 | 164 | 12 | inferred_complete_timeline |
| `Action_None` | 175 | 257 | 83 | inferred_complete_timeline |
| `Action_None` | 259 | 359 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 4–359
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 98 | 95 | inferred_complete_timeline |
| `Action_None` | 99 | 150 | 52 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 177 | 206 | 30 | inferred_complete_timeline |
| `Action_None` | 208 | 279 | 72 | inferred_complete_timeline |
| `Action_None` | 281 | 328 | 48 | inferred_complete_timeline |
| `Action_None` | 350 | 359 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 4–206
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 98 | 95 | inferred_complete_timeline |
| `Action_None` | 99 | 151 | 53 | inferred_complete_timeline |
| `Action_None` | 153 | 166 | 14 | inferred_complete_timeline |
| `Action_None` | 172 | 183 | 12 | inferred_complete_timeline |
| `Action_None` | 200 | 206 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 4–352
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 98 | 95 | inferred_complete_timeline |
| `Action_None` | 99 | 336 | 238 | inferred_complete_timeline |
| `Action_None` | 338 | 340 | 3 | inferred_complete_timeline |
| `Action_None` | 351 | 352 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 4–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 98 | 95 | inferred_complete_timeline |
| `Action_None` | 99 | 161 | 63 | inferred_complete_timeline |
| `Action_None` | 163 | 175 | 13 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 223 | 42 | inferred_complete_timeline |
| `Action_None` | 231 | 359 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 4–158
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 98 | 95 | inferred_complete_timeline |
| `Action_None` | 99 | 158 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 4–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 98 | 95 | inferred_complete_timeline |
| `Action_None` | 99 | 359 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 4–164
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 98 | 95 | inferred_complete_timeline |
| `Action_None` | 99 | 144 | 46 | inferred_complete_timeline |
| `Action_None` | 146 | 164 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 154–359 | 206 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 176–314 | 133 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 178–187 | 7 | 2 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 181–223 | 35 | 5 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 191–359 | 165 | 4 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 193–211 | 6 | 2 | Undefined position; Undefined team |
| `28` | `28` | Position_Unknown | Team_Unknown | 209–266 | 53 | 4 | Undefined position; Undefined team |
| `29` | `29` | Position_Unknown | Team_Unknown | 210–359 | 144 | 3 | Undefined position; Undefined team |
| `30` | `30` | Position_Unknown | Team_Unknown | 212–213 | 2 | 1 | Undefined position; Undefined team |
| `31` | `31` | Position_Unknown | Team_Unknown | 230–359 | 127 | 2 | Undefined position; Undefined team |
| `32` | `32` | Position_Unknown | Team_Unknown | 233–262 | 30 | 1 | Undefined position; Undefined team |
| `33` | `33` | Position_Unknown | Team_Unknown | 238–359 | 122 | 1 | Undefined position; Undefined team |
| `34` | `34` | Position_Unknown | Team_Unknown | 247–359 | 104 | 3 | Undefined position; Undefined team |
| `35` | `35` | Position_Unknown | Team_Unknown | 256–314 | 4 | 2 | Undefined position; Undefined team |
| `36` | `37` | Position_Unknown | Team_Unknown | 263–356 | 83 | 3 | Undefined position; Undefined team |
| `37` | `39` | Position_Unknown | Team_Unknown | 279–285 | 7 | 1 | Undefined position; Undefined team |
| `38` | `40` | Position_Unknown | Team_Unknown | 279–359 | 76 | 3 | Undefined position; Undefined team |
| `39` | `41` | Position_Unknown | Team_Unknown | 305–358 | 54 | 1 | Undefined position; Undefined team |
| `40` | `43` | Position_Unknown | Team_Unknown | 323–359 | 35 | 2 | Undefined position; Undefined team |
| `41` | `44` | Position_Unknown | Team_Unknown | 323–327 | 5 | 1 | Undefined position; Undefined team |
| `42` | `45` | Position_Unknown | Team_Unknown | 344–359 | 15 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (7 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `20` (RB): Annotated start 155 != Inferred start 179

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 113 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 93 frames exceeds threshold 90 frames [start=102, end=194].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (RG) duration 102 frames exceeds threshold 90 frames [start=102, end=203].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 102 frames exceeds threshold 90 frames [start=102, end=203].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [99–116], lower_priority='Action_ZoneBlock' annotated_start=102, effective_Action_ZoneBlock_start=117.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LT) duration 102 frames exceeds threshold 90 frames [start=102, end=203].
- ⚠️ Action 'Action_None' range [99-144] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-194] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-151] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-166] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-183] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-112] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-133] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-151] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-164] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-257] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-161] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-223] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-359] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-279] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-328] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-293] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-318] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-339] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-98] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-144] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-164] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-340] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-336] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-340] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [105-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-359] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-228] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [190-194] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 204, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [204-359] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-129] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [131-161] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-168] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [172-183] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [186-203] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [126-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-118] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-129] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [131-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-146] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [155-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [170-175] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-293] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-359] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-98] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-346] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [179-182] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-6] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-129] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-359] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-228] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-314] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-203] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-219] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-248] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-223] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-266] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-219] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-236] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-359] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-262] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-263] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-331] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-339] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-356] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-285] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-350] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-355] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-358] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-327] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-349] for track '42' has 1 frames without a visible bounding box.
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

</details>