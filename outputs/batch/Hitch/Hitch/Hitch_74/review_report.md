# Play-Annotation-Generator Annotation Review — Hitch_74

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_74`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 144
- **Validation Warnings:** 160
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 122
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_RunHitchRoute` | WR1 | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 11 | START | 11 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `13` | `13` | 14 | START | 14 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `15` | 14 | START | 26 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 14 | START | 14 | 42 |
| ✅ EXACT | `Action_PassBlock` | LT | `19` | `19` | 14 | START | 14 | 89 |
| ✅ EXACT | `Action_PassBlock` | RG | `20` | `20` | 14 | START | 14 | 52 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 25 | END | 11 | 25 |
| ✅ EXACT | `Action_RunHitchRoute` | WR1 | `3` | `3` | 31 | START | 31 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | `17` | `17` | 86 | START | 86 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `3` | `3` | 132 | START | 132 | 210 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 25 | 15 | inferred_complete_timeline |
| `Action_None` | 26 | 77 | 52 | inferred_complete_timeline |
| `Action_None` | 82 | 85 | 4 | inferred_complete_timeline |
| `Action_ThrowPass` | 86 | 92 | 7 | inferred_complete_timeline |
| `Action_ThrowPass` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 96 | 116 | 21 | inferred_complete_timeline |
| `Action_None` | 188 | 251 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 10 | 7 | inferred_complete_timeline |
| `Action_None` | 11 | 68 | 58 | inferred_complete_timeline |
| `Action_None` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_None` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_None` | 112 | 229 | 118 | inferred_complete_timeline |
| `Action_None` | 231 | 248 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 31 | 113 | 83 | inferred_complete_timeline |
| `Action_None` | 114 | 131 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 132 | 210 | 79 | inferred_complete_timeline |
| `Action_BallCarry` | 220 | 222 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 232 | 244 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 89 | 79 | inferred_complete_timeline |
| `Action_None` | 91 | 96 | 6 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_None` | 128 | 132 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 80 | 70 | inferred_complete_timeline |
| `Action_None` | 82 | 97 | 16 | inferred_complete_timeline |
| `Action_None` | 99 | 103 | 5 | inferred_complete_timeline |
| `Action_None` | 110 | 113 | 4 | inferred_complete_timeline |
| `Action_None` | 116 | 227 | 112 | inferred_complete_timeline |
| `Action_None` | 240 | 243 | 4 | inferred_complete_timeline |
| `Action_None` | 262 | 264 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 164 | 154 | inferred_complete_timeline |
| `Action_None` | 168 | 269 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 89 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 42 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 69 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 25 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 36 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 42 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 59 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 65 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 52 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 58 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 73 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 85 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 122 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 58 | 48 | inferred_complete_timeline |
| `Action_None` | 62 | 66 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 59 | 49 | inferred_complete_timeline |
| `Action_None` | 69 | 77 | 9 | inferred_complete_timeline |
| `Action_None` | 80 | 87 | 8 | inferred_complete_timeline |
| `Action_None` | 89 | 96 | 8 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 114 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 122 | 112 | inferred_complete_timeline |
| `Action_None` | 130 | 166 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 101 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 150 | 140 | inferred_complete_timeline |
| `Action_None` | 152 | 222 | 71 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 211 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 119 | 109 | inferred_complete_timeline |
| `Action_None` | 122 | 128 | 7 | inferred_complete_timeline |
| `Action_None` | 132 | 136 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 269 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 247 | 237 | inferred_complete_timeline |
| `Action_None` | 250 | 269 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 269 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 227 | 217 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 59–64 | 6 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 81–162 | 53 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 112–269 | 156 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 119–122 | 4 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 136–269 | 119 | 3 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 139–269 | 131 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 140–158 | 7 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 172–261 | 55 | 2 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 176–209 | 27 | 2 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 178–269 | 80 | 5 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 180–182 | 3 | 1 | Undefined position; Undefined team |
| `34` | `36` | Position_Unknown | Team_Unknown | 181–269 | 55 | 5 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 184–191 | 8 | 1 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 189–242 | 29 | 4 | Undefined position; Undefined team |
| `37` | `40` | Position_Unknown | Team_Unknown | 196–250 | 47 | 2 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 204–269 | 46 | 3 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 228–229 | 2 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 242–255 | 13 | 2 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 243–269 | 27 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 246–256 | 11 | 1 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 252–269 | 18 | 1 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 259–269 | 11 | 1 | Undefined position; Undefined team |
| `45` | `54` | Position_Unknown | Team_Unknown | 261–268 | 7 | 2 | Undefined position; Undefined team |
| `46` | `55` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ThrowPass` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 108 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [11–25], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=26.
- ⚠️ Action 'Action_None' range [11-164] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-269] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-89] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-96] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-132] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-247] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-269] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [132-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [220-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [226-227] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [232-244] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-119] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-128] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-211] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-58] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-66] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-80] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-97] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-227] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-227] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-222] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-59] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-87] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-58] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-73] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [82-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-122] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-122] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-166] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [86-92] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-116] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-251] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-42] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-89] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-52] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-68] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-229] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-248] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-64] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-111] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-154] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-235] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-182] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-217] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-261] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-187] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-209] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-217] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-269] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-192] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-204] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-223] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-248] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-191] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-223] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-250] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-215] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-229] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-255] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-269] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-256] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '45' has 2 frames without a visible bounding box.
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

</details>