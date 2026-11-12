# Play-Annotation-Generator Annotation Review — SplitZone_203

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_203`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 168
- **Validation Warnings:** 193
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 147
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `12` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 2 | START | 3 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 2 | START | 3 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 2 | START | 3 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 2 | START | 3 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `13` | `Group` | 2 | START | 3 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 2 | START | 3 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 2 | START | 3 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 2 | START | 3 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 2 | START | 3 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 2 | START | 3 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 2 | START | 3 | 131 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 129 | START | 129 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `11` | 132 | START | 143 | 143 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `16` | `16` | 132 | START | 132 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `17` | `17` | 132 | START | 132 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 132 | START | 132 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `4` | 132 | START | 132 | 143 |
| ✅ EXACT | `Action_SplitBlock` | HB | `13` | `13` | 141 | START | 141 | 175 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 142 | END | 129 | 142 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `18` | 152 | START | 152 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `12` | `12` | 163 | START | 163 | 188 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 205 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 3–292
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_SnapReceive` | 129 | 142 | 14 | inferred_complete_timeline |
| `Action_None` | 143 | 151 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 152 | 162 | 11 | inferred_complete_timeline |
| `Action_None` | 163 | 280 | 118 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 289 | 292 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 3–197
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 162 | 160 | inferred_complete_timeline |
| `Action_BallCarry` | 163 | 188 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 196 | 197 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 3–175
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 140 | 138 | inferred_complete_timeline |
| `Action_SplitBlock` | 141 | 175 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 3–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_None` | 129 | 280 | 152 | inferred_complete_timeline |
| `Action_None` | 283 | 287 | 5 | inferred_complete_timeline |
| `Action_None` | 292 | 389 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 3–389
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_None` | 129 | 257 | 129 | inferred_complete_timeline |
| `Action_None` | 259 | 260 | 2 | inferred_complete_timeline |
| `Action_None` | 270 | 389 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 3–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_None` | 129 | 389 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 3–389
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 131 | 129 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 143 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 172 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 185 | 6 | inferred_complete_timeline |
| `Action_None` | 209 | 242 | 34 | inferred_complete_timeline |
| `Action_None` | 245 | 389 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 3–143
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 131 | 129 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 143 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 3–185
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_BallSnap` | 129 | 142 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 143 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 184 | 185 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 3–172
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 131 | 129 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 142 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 172 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 3–237
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 131 | 129 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 143 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 160 | 5 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 3–172
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_None` | 129 | 143 | 15 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 172 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 3–172
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_None` | 129 | 152 | 24 | inferred_complete_timeline |
| `Action_None` | 170 | 172 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 3–202
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_None` | 129 | 143 | 15 | inferred_complete_timeline |
| `Action_None` | 160 | 162 | 3 | inferred_complete_timeline |
| `Action_None` | 165 | 175 | 11 | inferred_complete_timeline |
| `Action_None` | 180 | 186 | 7 | inferred_complete_timeline |
| `Action_None` | 195 | 199 | 5 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 3–237
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_None` | 129 | 143 | 15 | inferred_complete_timeline |
| `Action_None` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_None` | 150 | 157 | 8 | inferred_complete_timeline |
| `Action_None` | 159 | 188 | 30 | inferred_complete_timeline |
| `Action_None` | 191 | 193 | 3 | inferred_complete_timeline |
| `Action_None` | 196 | 202 | 7 | inferred_complete_timeline |
| `Action_None` | 233 | 237 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 3–150
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_None` | 129 | 143 | 15 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 3–202
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_None` | 129 | 145 | 17 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 3–202
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_None` | 129 | 202 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 3–251
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_None` | 129 | 251 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 3–373
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_None` | 129 | 362 | 234 | inferred_complete_timeline |
| `Action_None` | 365 | 373 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 3–202
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 135 | 4 | inferred_complete_timeline |
| `Action_None` | 137 | 168 | 32 | inferred_complete_timeline |
| `Action_None` | 170 | 172 | 3 | inferred_complete_timeline |
| `Action_None` | 180 | 186 | 7 | inferred_complete_timeline |
| `Action_None` | 195 | 202 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_None` | 129 | 366 | 238 | inferred_complete_timeline |
| `Action_None` | 371 | 389 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 161–238 | 34 | 5 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 197–202 | 6 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 203–356 | 149 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 213–215 | 3 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 218–256 | 30 | 5 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 220–389 | 166 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 242–243 | 2 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 249–389 | 140 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 253–389 | 98 | 6 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 255–389 | 122 | 3 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 257–259 | 3 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 266–389 | 123 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 268–273 | 6 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 268–389 | 122 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 276–389 | 108 | 4 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 277–389 | 108 | 4 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 278–389 | 102 | 3 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 278–389 | 112 | 1 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 278–372 | 54 | 11 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 278–389 | 92 | 5 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 281–389 | 102 | 4 | Undefined position; Undefined team |
| `45` | `57` | Position_Unknown | Team_Unknown | 282–310 | 9 | 3 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 290–332 | 43 | 1 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 294–389 | 93 | 3 | Undefined position; Undefined team |
| `48` | `62` | Position_Unknown | Team_Unknown | 300–341 | 8 | 3 | Undefined position; Undefined team |
| `49` | `64` | Position_Unknown | Team_Unknown | 313–314 | 2 | 1 | Undefined position; Undefined team |
| `50` | `69` | Position_Unknown | Team_Unknown | 359–360 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 133 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [129–142], lower_priority='Action_ZoneBlock' annotated_start=132, effective_Action_ZoneBlock_start=143.
- ⚠️ Action 'Action_None' range [129-389] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-280] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-257] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-251] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-143] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [145-146] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [156-160] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-366] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-152] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-362] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-373] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-202] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-168] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-186] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-202] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '11' starts at frame 143, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [143-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [180-182] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [184-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [163-188] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [196-197] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [141-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-145] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-143] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-188] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-237] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-143] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [180-185] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-242] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-389] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-280] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-143] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-175] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-186] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [170-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-175] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-343] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-356] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-237] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-256] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-237] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-249] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-389] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-372] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-389] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-275] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-287] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-309] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-361] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-259] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-289] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-275] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-273] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-371] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-384] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-289] for track '39' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-371] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-384] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-284] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-384] for track '40' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-389] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-284] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-305] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-316] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-333] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-352] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-286] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-368] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-374] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-286] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-382] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-389] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-310] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-332] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-298] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-380] for track '47' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-316] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-341] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '50' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.

</details>