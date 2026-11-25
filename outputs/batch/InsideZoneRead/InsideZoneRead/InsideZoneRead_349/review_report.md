# Play-Annotation-Generator Annotation Review — InsideZoneRead_349

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_349`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 101
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB3 | defense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `6` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_ReadDefender` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_Keep` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | RT | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_BallSnap` | CB3 | `12` | `11` | 16 | START | 16 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `12` | 19 | START | 19 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 19 | START | 19 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `22` | `21` | 19 | START | 19 | 37 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `6` | 19 | START | 19 | 86 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `8` | `7` | 19 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | RT | `8` | `7` | 29 | END | 16 | 29 |
| ✅ EXACT | `Action_ReadDefender` | RT | `8` | `7` | 40 | START | 40 | 43 |
| ✅ EXACT | `Action_Keep` | RT | `8` | `7` | 44 | START | 44 | 65 |
| ✅ EXACT | `Action_BallCarry` | RT | `8` | `7` | 66 | START | 66 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 86 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 125 | 110 | inferred_complete_timeline |
| `Action_None` | 128 | 210 | 83 | inferred_complete_timeline |
| `Action_None` | 215 | 269 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 40 | 25 | inferred_complete_timeline |
| `Action_None` | 42 | 62 | 21 | inferred_complete_timeline |
| `Action_None` | 64 | 76 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 248 | 233 | inferred_complete_timeline |
| `Action_None` | 250 | 269 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 86 | 68 | inferred_complete_timeline |
| `Action_None` | 87 | 269 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 40 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 63 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 37 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 86 | 28 | inferred_complete_timeline |
| `Action_None` | 87 | 170 | 84 | inferred_complete_timeline |
| `Action_None` | 172 | 196 | 25 | inferred_complete_timeline |
| `Action_None` | 205 | 241 | 37 | inferred_complete_timeline |
| `Action_None` | 244 | 269 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 19 | 74 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 86 | 11 | inferred_complete_timeline |
| `Action_None` | 87 | 130 | 44 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 226 | 84 | inferred_complete_timeline |
| `Action_None` | 236 | 269 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 29 | 14 | inferred_complete_timeline |
| `Action_None` | 30 | 39 | 10 | inferred_complete_timeline |
| `Action_ReadDefender` | 40 | 43 | 4 | inferred_complete_timeline |
| `Action_Keep` | 44 | 65 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 66 | 269 | 204 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 87 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 31 | 16 | inferred_complete_timeline |
| `Action_None` | 33 | 74 | 42 | inferred_complete_timeline |
| `Action_None` | 77 | 83 | 7 | inferred_complete_timeline |
| `Action_None` | 87 | 118 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 117 | 102 | inferred_complete_timeline |
| `Action_None` | 119 | 121 | 3 | inferred_complete_timeline |
| `Action_None` | 123 | 130 | 8 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_None` | 137 | 198 | 62 | inferred_complete_timeline |
| `Action_None` | 200 | 202 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_None` | 209 | 221 | 13 | inferred_complete_timeline |
| `Action_None` | 227 | 229 | 3 | inferred_complete_timeline |
| `Action_None` | 232 | 237 | 6 | inferred_complete_timeline |
| `Action_None` | 245 | 269 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 71 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_BallSnap` | 16 | 29 | 14 | inferred_complete_timeline |
| `Action_None` | 30 | 121 | 92 | inferred_complete_timeline |
| `Action_None` | 123 | 169 | 47 | inferred_complete_timeline |
| `Action_None` | 173 | 184 | 12 | inferred_complete_timeline |
| `Action_None` | 194 | 201 | 8 | inferred_complete_timeline |
| `Action_None` | 206 | 269 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 93 | 78 | inferred_complete_timeline |
| `Action_None` | 95 | 105 | 11 | inferred_complete_timeline |
| `Action_None` | 109 | 166 | 58 | inferred_complete_timeline |
| `Action_None` | 169 | 269 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 143 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 47 | 32 | inferred_complete_timeline |
| `Action_None` | 49 | 135 | 87 | inferred_complete_timeline |
| `Action_None` | 138 | 269 | 132 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 38–39 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 52–58 | 7 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 55–59 | 5 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 62–269 | 203 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 82–269 | 188 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 85–269 | 182 | 3 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 100–269 | 167 | 2 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 126–269 | 144 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 147–255 | 29 | 5 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 148–157 | 10 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 168–269 | 97 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 211–213 | 3 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 217–218 | 2 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 258–269 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `8` (RT)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '7' has invalid range: start=19, end=15. Clamping end to start.
- ⚠️ Action 'Action_None' range [16-248] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [16-29] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-31] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-74] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-83] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-105] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-166] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-169] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-201] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-74] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-130] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-226] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-130] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-198] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-221] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-237] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-47] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-143] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-40] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-63] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [19-37] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-43] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-86] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-196] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-241] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-58] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-59] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-70] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-165] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-269] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-250] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-237] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-248] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-255] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-157] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-269] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '35' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_349'; source metadata written as null.

</details>