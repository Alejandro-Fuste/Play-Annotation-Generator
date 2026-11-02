# Play-Annotation-Generator Annotation Review — JetSweep_219

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_219`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `4` | `3` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_LeadBlock` | TE2 | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `19` | `18` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_Toss` | QB | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `20` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 81 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `4` | `3` | 60 | START | 60 | 106 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 81 | START | 81 | 89 |
| ✅ EXACT | `Action_LeadBlock` | TE2 | `20` | `19` | 82 | START | 82 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `17` | 82 | START | 82 | 96 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `19` | `18` | 82 | START | 82 | 89 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `21` | `20` | 82 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `3` | `2` | 82 | START | 82 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `8` | 82 | START | 82 | 91 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `1` | 95 | END | 81 | 95 |
| ✅ EXACT | `Action_Toss` | QB | `2` | `1` | 100 | START | 100 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `4` | `3` | 107 | START | 107 | 108 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 144 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_SnapReceive` | 81 | 95 | 15 | inferred_complete_timeline |
| `Action_None` | 96 | 99 | 4 | inferred_complete_timeline |
| `Action_Toss` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_None` | 111 | 269 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 269 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 227 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_JetMotion` | 60 | 106 | 47 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 112 | 147 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 153 | 188 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 191 | 206 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 89 | 9 | inferred_complete_timeline |
| `Action_None` | 149 | 156 | 8 | inferred_complete_timeline |
| `Action_None` | 160 | 178 | 19 | inferred_complete_timeline |
| `Action_None` | 180 | 187 | 8 | inferred_complete_timeline |
| `Action_None` | 189 | 269 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_LeadBlock` | 82 | 90 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 89 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 96 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_BallSnap` | 81 | 89 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 91 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 103 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 93 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 106 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_None` | 148 | 269 | 122 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 89 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 89 | 9 | inferred_complete_timeline |
| `Action_None` | 124 | 133 | 10 | inferred_complete_timeline |
| `Action_None` | 140 | 269 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 89 | 9 | inferred_complete_timeline |
| `Action_None` | 113 | 115 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 128 | 48 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_None` | 148 | 156 | 9 | inferred_complete_timeline |
| `Action_None` | 160 | 162 | 3 | inferred_complete_timeline |
| `Action_None` | 165 | 178 | 14 | inferred_complete_timeline |
| `Action_None` | 181 | 228 | 48 | inferred_complete_timeline |
| `Action_None` | 232 | 235 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 144 | 64 | inferred_complete_timeline |
| `Action_None` | 147 | 156 | 10 | inferred_complete_timeline |
| `Action_None` | 158 | 227 | 70 | inferred_complete_timeline |
| `Action_None` | 240 | 244 | 5 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 93 | 13 | inferred_complete_timeline |
| `Action_None` | 99 | 107 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 233 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 136 | 56 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_None` | 154 | 208 | 55 | inferred_complete_timeline |
| `Action_None` | 212 | 220 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 233 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 158 | 78 | inferred_complete_timeline |
| `Action_None` | 160 | 200 | 41 | inferred_complete_timeline |
| `Action_None` | 208 | 238 | 31 | inferred_complete_timeline |
| `Action_None` | 242 | 269 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 93 | 13 | inferred_complete_timeline |
| `Action_None` | 95 | 269 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 107–109 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 124–200 | 63 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 137–269 | 124 | 5 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 137–269 | 130 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 139–266 | 128 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 149–257 | 21 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 152–269 | 113 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 154–266 | 107 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 182–269 | 78 | 4 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 182–244 | 60 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 243–269 | 27 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `21` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [81–89], lower_priority='Action_ZoneBlock' annotated_start=82, effective_Action_ZoneBlock_start=90.
- ⚠️ Action 'Action_None' range [81-233] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [100-102] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-93] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-96] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-106] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [107-108] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-147] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [153-188] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [191-206] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-227] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-89] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-158] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-238] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-89] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-91] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-103] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-233] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-93] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-107] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-208] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-89] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-156] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-89] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-227] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-244] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-96] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-89] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [82-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [81-89] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-156] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-178] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-228] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-134] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-160] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-156] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-246] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-247] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-266] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-228] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-242] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-263] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-236] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-244] for track '31' has 1 frames without a visible bounding box.
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

</details>