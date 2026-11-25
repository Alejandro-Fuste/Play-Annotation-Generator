# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_131

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_131`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 154
- **Validation Warnings:** 185
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `15` | `15` |
| ✅ EXACT | `Action_Handoff` | LB2 | defense | `10` | `10` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `5` | `5` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 176 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `2` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `15` | `15` | 29 | START | 29 | 58 |
| ✅ EXACT | `Action_Handoff` | LB2 | `10` | `10` | 57 | START | 57 | 73 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `13` | `13` | 186 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `18` | 186 | START | 186 | 188 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `20` | 186 | START | 186 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `5` | `5` | 186 | START | 186 | 212 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `7` | `7` | 186 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 163 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 225 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 238 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 241 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 258 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 289 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 296 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PressEdge` | 29 | 58 | 30 | inferred_complete_timeline |
| `Action_PressEdge` | 63 | 66 | 4 | inferred_complete_timeline |
| `Action_PressEdge` | 74 | 166 | 93 | inferred_complete_timeline |
| `Action_None` | 167 | 283 | 117 | inferred_complete_timeline |
| `Action_None` | 286 | 296 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 144 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 153 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 165 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–280
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 186 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 206 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 220 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 241 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 253 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 262 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 269 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 277 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 280 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 277 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 299 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 73 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 90 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 118 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 135 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 147 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 153 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 159 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 181 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 188 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 198 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 267 | 3 | inferred_complete_timeline |
| `Action_None` | 281 | 284 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 121 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 132 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 153 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 185 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 233 | 48 | inferred_complete_timeline |
| `Action_None` | 234 | 268 | 35 | inferred_complete_timeline |
| `Action_None` | 270 | 297 | 28 | inferred_complete_timeline |
| `Action_None` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 46 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 55 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 64 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 112 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 158 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 185 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 212 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 229 | 232 | 4 | inferred_complete_timeline |
| `Action_None` | 236 | 238 | 3 | inferred_complete_timeline |
| `Action_None` | 248 | 255 | 8 | inferred_complete_timeline |
| `Action_None` | 259 | 260 | 2 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 296 | 298 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 70 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 299 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 190 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 199 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 206 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 215 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 233 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 246 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 250 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 299 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_Handoff` | 57 | 73 | 17 | inferred_complete_timeline |
| `Action_None` | 74 | 154 | 81 | inferred_complete_timeline |
| `Action_None` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 299 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 178 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 299 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–299 | 298 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 64–69 | 6 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 67–163 | 94 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 75–296 | 162 | 11 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 78–214 | 131 | 4 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 81–82 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 98–126 | 29 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 114–115 | 2 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 169–186 | 16 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 174–203 | 28 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 210–299 | 72 | 7 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 211–262 | 51 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 212–214 | 3 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 241–258 | 8 | 2 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 245–246 | 2 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 248–299 | 48 | 4 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 271–273 | 3 | 1 | Undefined position; Undefined team |
| `39` | `60` | Position_Unknown | Team_Unknown | 294–296 | 3 | 1 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PressEdge` and target `15` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `13` (RG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `7` (RT)

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 139 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '7' has invalid range: start=186, end=53. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '13' has invalid range: start=186, end=70. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-277] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-299] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-144] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-186] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-206] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-220] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-241] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-253] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-262] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-277] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-280] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-144] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-153] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-165] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-299] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-46] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-55] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-64] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-112] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-158] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-185] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [186-212] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [214-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [229-232] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-255] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-186] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-154] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-163] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-225] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-238] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-241] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-258] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-289] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-296] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-70] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-293] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-297] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [29-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [63-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-283] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-296] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-148] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-178] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-118] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-147] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-153] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-159] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-181] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [186-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [196-198] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-132] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-153] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [186-233] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-268] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-297] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-182] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-190] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-194] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-199] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-206] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-215] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-233] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-246] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-250] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-299] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-69] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-73] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-163] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-80] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-158] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-168] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-176] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-194] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-223] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-234] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-238] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-276] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-283] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-296] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-160] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-199] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-214] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-126] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-115] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-181] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-186] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-194] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-203] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-212] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-229] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-259] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-270] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-279] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-287] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-299] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-217] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-262] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-214] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-244] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-258] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-252] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-260] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-284] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-299] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-273] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-296] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'OutsideZoneStretch_131'; source metadata written as null.

</details>