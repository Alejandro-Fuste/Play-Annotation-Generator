# Play-Annotation-Generator Annotation Review — InsideZoneRead_265

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_265`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 126
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Keep` | QB | offense | `18` | `17` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | RG | offense | `16` | `15` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `8` | `Group` | 0 | START | 0 | 16 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 17 | START | 17 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `11` | 20 | START | 20 | 102 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `13` | `12` | 20 | START | 20 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `14` | 20 | START | 32 | 101 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `16` | `15` | 20 | START | 20 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 20 | START | 20 | 52 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 31 | END | 17 | 31 |
| ✅ EXACT | `Action_ReadDefender` | QB | `18` | `17` | 35 | START | 35 | 48 |
| ✅ EXACT | `Action_Keep` | QB | `18` | `17` | 49 | START | 49 | 68 |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | RG | `16` | `15` | 62 | START | 74 | 102 |
| ✅ EXACT | `Action_BallCarry` | QB | `18` | `17` | 69 | START | 69 | 132 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 102 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 31 | 15 | inferred_complete_timeline |
| `Action_None` | 32 | 34 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 35 | 48 | 14 | inferred_complete_timeline |
| `Action_Keep` | 49 | 68 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 69 | 132 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 53 | 37 | inferred_complete_timeline |
| `Action_None` | 56 | 123 | 68 | inferred_complete_timeline |
| `Action_None` | 129 | 223 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 208 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 89 | 73 | inferred_complete_timeline |
| `Action_None` | 91 | 147 | 57 | inferred_complete_timeline |
| `Action_None` | 150 | 153 | 4 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 197 | 38 | inferred_complete_timeline |
| `Action_None` | 199 | 231 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 89 | 73 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_None` | 99 | 101 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 94 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 52 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 100 | 7 | inferred_complete_timeline |
| `Action_None` | 109 | 231 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_BallSnap` | 17 | 31 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 101 | 70 | inferred_complete_timeline |
| `Action_None` | 112 | 214 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 40 | 21 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 74 | 102 | 29 | inferred_complete_timeline |
| `Action_None` | 103 | 114 | 12 | inferred_complete_timeline |
| `Action_None` | 118 | 124 | 7 | inferred_complete_timeline |
| `Action_None` | 126 | 178 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 102 | 83 | inferred_complete_timeline |
| `Action_None` | 103 | 211 | 109 | inferred_complete_timeline |
| `Action_None` | 214 | 239 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 103 | 87 | inferred_complete_timeline |
| `Action_None` | 110 | 122 | 13 | inferred_complete_timeline |
| `Action_None` | 124 | 214 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 239 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 75 | 59 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 239 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 105 | 89 | inferred_complete_timeline |
| `Action_None` | 110 | 119 | 10 | inferred_complete_timeline |
| `Action_None` | 122 | 138 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 170 | 154 | inferred_complete_timeline |
| `Action_None` | 174 | 187 | 14 | inferred_complete_timeline |
| `Action_None` | 189 | 191 | 3 | inferred_complete_timeline |
| `Action_None` | 193 | 214 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 101 | 85 | inferred_complete_timeline |
| `Action_None` | 105 | 112 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 50 | 34 | inferred_complete_timeline |
| `Action_None` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_None` | 59 | 71 | 13 | inferred_complete_timeline |
| `Action_None` | 82 | 94 | 13 | inferred_complete_timeline |
| `Action_None` | 96 | 163 | 68 | inferred_complete_timeline |
| `Action_None` | 167 | 214 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 158 | 142 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 208 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 211 | 195 | inferred_complete_timeline |
| `Action_None` | 214 | 239 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 52–107 | 56 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 117–239 | 123 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 131–208 | 78 | 1 | Undefined position; Undefined team |
| `25` | `40` | Position_Unknown | Team_Unknown | 138–221 | 84 | 1 | Undefined position; Undefined team |
| `26` | `41` | Position_Unknown | Team_Unknown | 138–211 | 74 | 1 | Undefined position; Undefined team |
| `27` | `42` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |
| `28` | `44` | Position_Unknown | Team_Unknown | 157–226 | 70 | 1 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 175–176 | 2 | 1 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 181–211 | 9 | 3 | Undefined position; Undefined team |
| `31` | `49` | Position_Unknown | Team_Unknown | 195–196 | 2 | 1 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 200–205 | 5 | 2 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 209–211 | 3 | 1 | Undefined position; Undefined team |
| `34` | `52` | Position_Unknown | Team_Unknown | 212–213 | 2 | 1 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 215–216 | 2 | 1 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 215–239 | 25 | 1 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 215–239 | 25 | 1 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 218–221 | 4 | 1 | Undefined position; Undefined team |
| `39` | `62` | Position_Unknown | Team_Unknown | 218–239 | 21 | 2 | Undefined position; Undefined team |
| `40` | `63` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |
| `41` | `66` | Position_Unknown | Team_Unknown | 222–223 | 2 | 1 | Undefined position; Undefined team |
| `42` | `67` | Position_Unknown | Team_Unknown | 222–226 | 5 | 1 | Undefined position; Undefined team |
| `43` | `68` | Position_Unknown | Team_Unknown | 222–224 | 3 | 1 | Undefined position; Undefined team |
| `44` | `73` | Position_Unknown | Team_Unknown | 232–237 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ `Action_BlockSecondLevel` for actor_track_id `16` (RG): Annotated start 62 != Inferred start 74

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [17–31], lower_priority='Action_ZoneBlock' annotated_start=20, effective_Action_ZoneBlock_start=32.
- ⚠️ Action 'Action_None' range [17-208] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-180] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-75] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-89] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-147] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-197] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-231] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-239] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-170] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-187] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-214] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-103] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-122] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-214] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-89] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-101] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-112] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-105] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-119] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-138] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-239] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-211] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-208] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-214] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-40] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-114] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-178] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-50] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-94] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-163] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-214] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [69-132] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-211] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-52] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-100] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-231] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-123] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-223] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-158] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-107] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-208] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-221] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-239] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-226] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-237] for track '44' has 1 frames without a visible bounding box.
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

</details>