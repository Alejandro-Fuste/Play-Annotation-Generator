# Play-Annotation-Generator Annotation Review — InsideZoneRead_243

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_243`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 130
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 103
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Keep` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 14 | START | 14 | 30 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `11` | `10` | 17 | START | 31 | 69 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `16` | 17 | START | 17 | 94 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `19` | `18` | 17 | START | 17 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `20` | 17 | START | 17 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 17 | START | 17 | 33 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 30 | END | 14 | 30 |
| ✅ EXACT | `Action_ReadDefender` | QB | `13` | `12` | 34 | START | 34 | 43 |
| ✅ EXACT | `Action_Keep` | QB | `13` | `12` | 44 | START | 44 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `13` | `12` | 56 | START | 56 | 197 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 94 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_SnapReceive` | 14 | 30 | 17 | inferred_complete_timeline |
| `Action_None` | 31 | 33 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 34 | 43 | 10 | inferred_complete_timeline |
| `Action_Keep` | 44 | 55 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 56 | 197 | 142 | inferred_complete_timeline |
| `Action_BallCarry` | 202 | 206 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 211 | 215 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 170 | 157 | inferred_complete_timeline |
| `Action_None` | 175 | 239 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 239 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 239 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 239 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 230 | 217 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 94 | 78 | inferred_complete_timeline |
| `Action_None` | 95 | 239 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 94 | 78 | inferred_complete_timeline |
| `Action_None` | 95 | 215 | 121 | inferred_complete_timeline |
| `Action_None` | 221 | 226 | 6 | inferred_complete_timeline |
| `Action_None` | 228 | 239 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_BallSnap` | 14 | 30 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 69 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 33 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 40 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 62 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 71 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 94 | 22 | inferred_complete_timeline |
| `Action_None` | 95 | 136 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 48 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 94 | 41 | inferred_complete_timeline |
| `Action_None` | 95 | 216 | 122 | inferred_complete_timeline |
| `Action_None` | 219 | 232 | 14 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 43 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 59 | 46 | inferred_complete_timeline |
| `Action_None` | 67 | 108 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 43 | 30 | inferred_complete_timeline |
| `Action_None` | 50 | 56 | 7 | inferred_complete_timeline |
| `Action_None` | 59 | 102 | 44 | inferred_complete_timeline |
| `Action_None` | 106 | 203 | 98 | inferred_complete_timeline |
| `Action_None` | 224 | 234 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 172 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 46 | 33 | inferred_complete_timeline |
| `Action_None` | 49 | 239 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 43 | 30 | inferred_complete_timeline |
| `Action_None` | 45 | 49 | 5 | inferred_complete_timeline |
| `Action_None` | 51 | 59 | 9 | inferred_complete_timeline |
| `Action_None` | 67 | 89 | 23 | inferred_complete_timeline |
| `Action_None` | 91 | 95 | 5 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_None` | 108 | 122 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 224 | 211 | inferred_complete_timeline |
| `Action_None` | 230 | 234 | 5 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 173 | 160 | inferred_complete_timeline |
| `Action_None` | 176 | 191 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 88 | 75 | inferred_complete_timeline |
| `Action_None` | 90 | 102 | 13 | inferred_complete_timeline |
| `Action_None` | 105 | 108 | 4 | inferred_complete_timeline |
| `Action_None` | 110 | 239 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 223 | 210 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–49 | 50 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 54–163 | 96 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 60–238 | 169 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 63–67 | 5 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 96–239 | 138 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 114–115 | 2 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 129–239 | 111 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 134–137 | 4 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 146–152 | 6 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 151–234 | 59 | 3 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 154–239 | 55 | 8 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 169–239 | 55 | 4 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 176–178 | 3 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 182–184 | 3 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 182–183 | 2 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 182–221 | 31 | 4 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 185–189 | 5 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 230–239 | 9 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `11` (C): Annotated start 17 != Inferred start 31
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (9 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (7 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (4 segments found)

### Track Identity Issues

- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 486: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [14–30], lower_priority='Action_ZoneBlock' annotated_start=17, effective_Action_ZoneBlock_start=31.
- ⚠️ Action 'Action_None' range [14-43] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-49] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-59] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-89] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-95] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-122] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-43] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-59] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-108] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-49] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-43] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-56] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-102] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-203] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-234] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-230] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-223] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-69] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-224] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [56-197] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [202-206] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [211-215] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-170] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-215] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-226] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-173] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-191] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-48] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-216] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-232] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-33] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-40] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [44-45] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-49] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-62] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-136] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-238] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-67] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-239] for track '27' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-215] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-234] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-175] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-193] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-236] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-189] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-208] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-215] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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

</details>