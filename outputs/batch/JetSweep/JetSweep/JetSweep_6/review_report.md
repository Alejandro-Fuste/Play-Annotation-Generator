# Play-Annotation-Generator Annotation Review — JetSweep_6

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `JetSweep_6`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 55
- **Ball Tracks:** 0
- **Action Segments:** 203
- **Validation Warnings:** 254
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 8
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 179
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT-1 | defense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR | offense | `19` | `16` |
| ⚠️ START CHANGED | `Action_Toss` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `19` | `16` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `11` | `10` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `11` | `10` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `14` | `13` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `18` | `15` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `9` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 26 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 30 |
| ✅ EXACT | `Action_BallSnap` | DT-1 | `12` | `11` | 31 | START | 31 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | `13` | `12` | 32 | START | 32 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `10` | `9` | 32 | START | 32 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 32 | START | 32 | 38 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `14` | `13` | 32 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `15` | 32 | START | 32 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `9` | `8` | 32 | START | 34 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR | `19` | `16` | 33 | START | 33 | 47 |
| ⚠️ START CHANGED | `Action_Toss` | C | `14` | `13` | 48 | START | 50 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | `10` | `9` | 52 | START | 52 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `19` | `16` | 62 | START | 68 | 97 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `11` | `10` | 99 | BOUNDARY | 88 | 99 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `11` | `10` | 99 | BOUNDARY | 88 | 99 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `14` | `13` | 99 | BOUNDARY | N/A | 99 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `18` | `15` | 99 | BOUNDARY | 85 | 99 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `9` | `8` | 99 | BOUNDARY | N/A | 99 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>WR — actor_track_id `19`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 33–121
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 33 | 47 | 15 | inferred_complete_timeline |
| `Action_JetMotion` | 49 | 60 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 68 | 97 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 113 | 121 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 139 | 109 | inferred_complete_timeline |
| `Action_None` | 141 | 190 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_LeadBlock` | 32 | 34 | 3 | inferred_complete_timeline |
| `Action_LeadBlock` | 40 | 41 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 36 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 51 | 6 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 64 | 65 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 26–269
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 31 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 42 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 99 | 15 | inferred_complete_timeline |
| `Action_None` | 100 | 168 | 69 | inferred_complete_timeline |
| `Action_None` | 170 | 263 | 94 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 13 | 3 | inferred_complete_timeline |
| `Action_Toss` | 50 | 61 | 12 | inferred_complete_timeline |
| `Action_None` | 62 | 141 | 80 | inferred_complete_timeline |
| `Action_None` | 149 | 172 | 24 | inferred_complete_timeline |
| `Action_None` | 178 | 269 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 38 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 58 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 77 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 99 | 12 | inferred_complete_timeline |
| `Action_None` | 100 | 119 | 20 | inferred_complete_timeline |
| `Action_None` | 121 | 160 | 40 | inferred_complete_timeline |
| `Action_None` | 163 | 175 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 36 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 76 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DT — actor_track_id `20`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 36–137
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 36 | 89 | 54 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 98 | 113 | 16 | inferred_complete_timeline |
| `Action_None` | 124 | 137 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT-1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_BallSnap` | 31 | 31 | 1 | inferred_complete_timeline |
| `Action_None` | 32 | 43 | 12 | inferred_complete_timeline |
| `Action_None` | 66 | 68 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LDE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 100 | 70 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RDE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 73 | 43 | inferred_complete_timeline |
| `Action_None` | 87 | 96 | 10 | inferred_complete_timeline |
| `Action_None` | 107 | 233 | 127 | inferred_complete_timeline |
| `Action_None` | 236 | 238 | 3 | inferred_complete_timeline |
| `Action_None` | 243 | 269 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 62 | 32 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_None` | 76 | 107 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 108 | 78 | inferred_complete_timeline |
| `Action_None` | 111 | 159 | 49 | inferred_complete_timeline |
| `Action_None` | 165 | 269 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 104 | 74 | inferred_complete_timeline |
| `Action_None` | 109 | 111 | 3 | inferred_complete_timeline |
| `Action_None` | 114 | 125 | 12 | inferred_complete_timeline |
| `Action_None` | 127 | 205 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 96 | 66 | inferred_complete_timeline |
| `Action_None` | 98 | 182 | 85 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 243 | 39 | inferred_complete_timeline |
| `Action_None` | 245 | 251 | 7 | inferred_complete_timeline |
| `Action_None` | 253 | 261 | 9 | inferred_complete_timeline |
| `Action_None` | 264 | 266 | 3 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 55 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `16` | Position_Unknown | Team_Unknown | 10–117 | 88 | 8 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 41–146 | 36 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 42–47 | 6 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 43–52 | 10 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 46–109 | 62 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 48–269 | 215 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 51–70 | 20 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 72–265 | 125 | 6 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 76–134 | 35 | 4 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 81–125 | 26 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 84–188 | 74 | 5 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 99–230 | 128 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 112–117 | 6 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 124–269 | 145 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 127–128 | 2 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 128–129 | 2 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 134–220 | 53 | 6 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 134–235 | 68 | 8 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 136–142 | 6 | 2 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 140–175 | 36 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 142–253 | 97 | 6 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 150–151 | 2 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 151–155 | 5 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 159–269 | 81 | 7 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 167–269 | 84 | 8 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 176–243 | 12 | 3 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 177–232 | 47 | 3 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 182–269 | 77 | 4 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 186–211 | 26 | 1 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 187–255 | 46 | 7 | Undefined position; Undefined team |
| `47` | `65` | Position_Unknown | Team_Unknown | 193–229 | 35 | 2 | Undefined position; Undefined team |
| `48` | `66` | Position_Unknown | Team_Unknown | 194–269 | 63 | 7 | Undefined position; Undefined team |
| `49` | `67` | Position_Unknown | Team_Unknown | 197–206 | 5 | 2 | Undefined position; Undefined team |
| `50` | `68` | Position_Unknown | Team_Unknown | 237–269 | 32 | 2 | Undefined position; Undefined team |
| `51` | `71` | Position_Unknown | Team_Unknown | 256–269 | 14 | 1 | Undefined position; Undefined team |
| `52` | `72` | Position_Unknown | Team_Unknown | 263–268 | 6 | 1 | Undefined position; Undefined team |
| `53` | `73` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |
| `54` | `75` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (4 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `14` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (5 segments found)
- ⚠️ Ambiguous match for action `Action_JetMotion` and target `19` (2 segments found)
- ⚠️ `Action_Toss` for actor_track_id `14` (C): Annotated start 48 != Inferred start 50
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_SnapReceive' at frame 42 targets track ID '[?]', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 174 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 13: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 13: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_BallSnap present in CSV, but paired Action_SnapReceive is missing.
- ⚠️ Action 'Action_None' range [31-96] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-182] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-243] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-251] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-261] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-62] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-107] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-108] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-159] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-104] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-205] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-55] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-100] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-190] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-73] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-233] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-36] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-76] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-36] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-43] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [52-54] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [64-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-38] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-58] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-119] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-160] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-175] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-43] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-68] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [32-34] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [40-41] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-13] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [50-61] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-11] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-30] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-33] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-81] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-108] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-263] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [33-47] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [49-60] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [68-97] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [113-121] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-113] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-137] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-67] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-52] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-75] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-167] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-70] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-82] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-97] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-149] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-240] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-265] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-134] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-95] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-125] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-134] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-173] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-218] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-117] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-246] for track '30' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-141] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-160] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-170] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-212] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-165] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-187] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-225] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-175] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-157] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-168] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-248] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-207] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-216] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-269] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-190] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-208] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-222] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-232] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-243] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-261] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-243] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-208] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-220] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-232] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-224] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-233] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-211] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-211] for track '46' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-224] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-204] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-219] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-232] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-242] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-269] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-266] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-268] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.

</details>