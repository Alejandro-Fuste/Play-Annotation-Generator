# Play-Annotation-Generator Annotation Review — BootPass_95

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_95`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 128
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `21` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_RunFlatRoute` | TE2 | offense | `12` | `12` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | TE2 | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `12` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `21` | `Group` | 0 | START | 0 | 7 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `19` | `19` | 8 | START | 8 | 16 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `15` | `15` | 16 | START | 16 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `17` | `17` | 16 | START | 16 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `18` | `18` | 16 | START | 16 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `19` | `19` | 16 | START | 25 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `20` | `20` | 16 | START | 16 | 34 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 24 | END | 8 | 24 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `16` | `16` | 30 | START | 30 | 51 |
| ✅ EXACT | `Action_RunFlatRoute` | TE2 | `12` | `12` | 49 | START | 49 | 71 |
| ✅ EXACT | `Action_BootAway` | QB | `16` | `16` | 52 | START | 52 | 62 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 63 | START | 63 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | TE2 | `12` | `12` | 81 | START | 81 | 85 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 8 | 24 | 17 | inferred_complete_timeline |
| `Action_None` | 25 | 29 | 5 | inferred_complete_timeline |
| `Action_FakeHandoff` | 30 | 51 | 22 | inferred_complete_timeline |
| `Action_BootAway` | 52 | 62 | 11 | inferred_complete_timeline |
| `Action_ThrowPass` | 63 | 74 | 12 | inferred_complete_timeline |
| `Action_None` | 75 | 200 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 81 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 269 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 269 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 75 | 68 | inferred_complete_timeline |
| `Action_None` | 96 | 99 | 4 | inferred_complete_timeline |
| `Action_None` | 105 | 132 | 28 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 49 | 71 | 23 | inferred_complete_timeline |
| `Action_None` | 72 | 80 | 9 | inferred_complete_timeline |
| `Action_SecureCatch` | 81 | 85 | 5 | inferred_complete_timeline |
| `Action_SecureCatch` | 91 | 91 | 1 | inferred_complete_timeline |
| `Action_None` | 92 | 269 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 16 | 81 | 66 | inferred_complete_timeline |
| `Action_RunBlock` | 83 | 88 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 93 | 97 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 16 | 34 | 19 | inferred_complete_timeline |
| `Action_RunBlock` | 49 | 115 | 67 | inferred_complete_timeline |
| `Action_RunBlock` | 117 | 149 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 8 | 16 | 9 | inferred_complete_timeline |
| `Action_BallSnap` | 18 | 24 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 25 | 75 | 51 | inferred_complete_timeline |
| `Action_RunBlock` | 77 | 105 | 29 | inferred_complete_timeline |
| `Action_RunBlock` | 107 | 112 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 115 | 149 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 16 | 65 | 50 | inferred_complete_timeline |
| `Action_RunBlock` | 69 | 71 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 16 | 34 | 19 | inferred_complete_timeline |
| `Action_RunBlock` | 39 | 49 | 11 | inferred_complete_timeline |
| `Action_RunBlock` | 51 | 56 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 66 | 68 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 70 | 152 | 83 | inferred_complete_timeline |
| `Action_RunBlock` | 154 | 155 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 47 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 38 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 36 | 29 | inferred_complete_timeline |
| `Action_None` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_None` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_None` | 64 | 124 | 61 | inferred_complete_timeline |
| `Action_None` | 155 | 172 | 18 | inferred_complete_timeline |
| `Action_None` | 175 | 179 | 5 | inferred_complete_timeline |
| `Action_None` | 194 | 204 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 79 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 91 | 84 | inferred_complete_timeline |
| `Action_None` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_None` | 101 | 150 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 268 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 269 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 231 | 224 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_None` | 238 | 242 | 5 | inferred_complete_timeline |
| `Action_None` | 253 | 265 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 205 | 198 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 228 | 232 | 5 | inferred_complete_timeline |
| `Action_None` | 237 | 241 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 269 | 262 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–155 | 138 | 6 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 58–59 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 74–104 | 13 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 74–77 | 4 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 74–75 | 2 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 84–185 | 89 | 5 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 93–132 | 10 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 111–168 | 52 | 4 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 122–150 | 28 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 133–150 | 11 | 3 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 143–149 | 7 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 164–167 | 4 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 201–220 | 20 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 203–255 | 37 | 7 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 240–247 | 8 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 254–255 | 2 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 258–268 | 5 | 2 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 261–269 | 9 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (6 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SecureCatch` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 94 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [8–24], lower_priority='Action_RunBlock' annotated_start=16, effective_Action_RunBlock_start=25.
- ⚠️ Action 'Action_None' range [8-205] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-268] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-36] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-124] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-172] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-204] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-38] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-79] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-231] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-242] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-265] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-100] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-115] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-81] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-269] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [81-85] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-269] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-47] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [16-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [69-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [16-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [83-88] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [93-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [100-269] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [16-34] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [39-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [51-56] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [66-68] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [70-152] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [154-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [8-16] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [18-24] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [25-75] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [77-105] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [107-112] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [115-149] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [16-34] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [49-115] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [117-149] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-75] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-92] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-103] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-173] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-168] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-149] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-211] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-223] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-245] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-247] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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