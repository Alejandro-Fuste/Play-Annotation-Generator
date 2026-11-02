# Play-Annotation-Generator Annotation Review — JetSweep_131

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_131`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 121
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `8` | `7` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | WR2 | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `22` | `20` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | offense | `23` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Toss` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `8` | `7` |
| ✅ EXACT | `Action_SealBlock` | TE1 | offense | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `19` | `Group` | 0 | START | 11 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 20 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 0 | START | 23 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 19 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `8` | `7` | 20 | START | 20 | 72 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `20` | 41 | START | 41 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | WR2 | `4` | `3` | 48 | START | 48 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `13` | 48 | START | 48 | 68 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `14` | 48 | START | 48 | 76 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `22` | `20` | 48 | START | 56 | 121 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | `23` | `21` | 48 | START | 49 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `16` | `15` | 55 | END | 41 | 44 |
| ✅ EXACT | `Action_Toss` | QB | `16` | `15` | 60 | START | 60 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `8` | `7` | 73 | START | 79 | 80 |
| ✅ EXACT | `Action_SealBlock` | TE1 | `18` | `17` | 76 | START | 76 | 215 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 121 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 40 | 6 | inferred_complete_timeline |
| `Action_SnapReceive` | 41 | 44 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 55 | 10 | inferred_complete_timeline |
| `Action_None` | 56 | 59 | 4 | inferred_complete_timeline |
| `Action_Toss` | 60 | 72 | 13 | inferred_complete_timeline |
| `Action_None` | 73 | 160 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_JetMotion` | 20 | 72 | 53 | inferred_complete_timeline |
| `Action_BallCarry` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 89 | 97 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 100 | 186 | 87 | inferred_complete_timeline |
| `Action_BallCarry` | 188 | 219 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 221 | 232 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 234 | 238 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_LeadBlock` | 48 | 89 | 42 | inferred_complete_timeline |
| `Action_LeadBlock` | 91 | 121 | 31 | inferred_complete_timeline |
| `Action_None` | 122 | 239 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 5 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 13 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 75 | 60 | inferred_complete_timeline |
| `Action_SealBlock` | 76 | 215 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 11–179
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 13 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 40 | 25 | inferred_complete_timeline |
| `Action_None` | 41 | 134 | 94 | inferred_complete_timeline |
| `Action_None` | 141 | 156 | 16 | inferred_complete_timeline |
| `Action_None` | 162 | 179 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 76 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 68 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 107 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 121 | 12 | inferred_complete_timeline |
| `Action_None` | 122 | 158 | 37 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 173 | 6 | inferred_complete_timeline |
| `Action_None` | 177 | 181 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 20–170
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 27 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 40 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 41 | 55 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 121 | 66 | inferred_complete_timeline |
| `Action_None` | 122 | 170 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 23–178
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 24 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 47 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 121 | 73 | inferred_complete_timeline |
| `Action_None` | 122 | 178 | 57 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 71 | 31 | inferred_complete_timeline |
| `Action_None` | 73 | 92 | 20 | inferred_complete_timeline |
| `Action_None` | 98 | 100 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 211 | 171 | inferred_complete_timeline |
| `Action_None` | 214 | 239 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 56 | 16 | inferred_complete_timeline |
| `Action_None` | 67 | 73 | 7 | inferred_complete_timeline |
| `Action_None` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 62 | 22 | inferred_complete_timeline |
| `Action_None` | 69 | 166 | 98 | inferred_complete_timeline |
| `Action_None` | 168 | 172 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 107 | 67 | inferred_complete_timeline |
| `Action_None` | 116 | 239 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 141 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 158 | 118 | inferred_complete_timeline |
| `Action_None` | 163 | 239 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 195 | 155 | inferred_complete_timeline |
| `Action_None` | 202 | 239 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 114 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 239 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 41 | 75 | 35 | inferred_complete_timeline |
| `Action_None` | 77 | 89 | 13 | inferred_complete_timeline |
| `Action_None` | 92 | 188 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–239 | 237 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 16–94 | 78 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 35–90 | 54 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 61–90 | 22 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 92–212 | 119 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 97–107 | 11 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 99–175 | 73 | 4 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 112–131 | 11 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 115–162 | 48 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 116–129 | 6 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 125–211 | 87 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 131–188 | 55 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 131–201 | 71 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 174–239 | 65 | 2 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 194–197 | 4 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 234–237 | 4 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 236–239 | 3 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `22` (C): Annotated start 48 != Inferred start 56
- ⚠️ `Action_ZoneBlock` for actor_track_id `23` (RG): Annotated start 48 != Inferred start 49
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 263: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [41–55], lower_priority='Action_ZoneBlock' annotated_start=48, effective_Action_ZoneBlock_start=56.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-75] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-89] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-188] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-114] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-195] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [48-89] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [91-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-107] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-141] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-56] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-73] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [20-72] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [79-80] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [89-97] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [100-186] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [188-219] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [221-232] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [234-238] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-62] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-166] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-71] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-158] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-179] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-211] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-68] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-107] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-158] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-181] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [41-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [46-55] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-160] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-13] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [76-215] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-13] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-134] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-179] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-18] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-94] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-27] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-40] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-170] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-47] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-178] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-62] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-78] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-204] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-107] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-138] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-148] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-156] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-175] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-162] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-211] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-146] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-188] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-201] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>