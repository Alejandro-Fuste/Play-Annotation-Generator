# Play-Annotation-Generator Annotation Review — JetSweep_123

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_123`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `3` | `2` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | offense | `21` | `20` |
| ⚠️ START CHANGED | `Action_Toss` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `19` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 51 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `3` | `2` | 25 | START | 25 | 75 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 50 | START | 50 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | RB | `7` | `6` | 52 | START | 52 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `13` | `12` | 52 | START | 52 | 73 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `22` | `21` | 52 | START | 52 | 86 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `22` | `21` | 52 | START | 52 | 86 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `3` | 52 | START | 52 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `8` | 52 | START | 52 | 79 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | `21` | `20` | 64 | END | N/A | N/A |
| ⚠️ START CHANGED | `Action_Toss` | C | `21` | `20` | 68 | START | 69 | 75 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `3` | `2` | 76 | START | 76 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `22` | `21` | 87 | START | 87 | 121 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 167 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 239 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_LeadBlock` | 52 | 147 | 96 | inferred_complete_timeline |
| `Action_LeadBlock` | 150 | 167 | 18 | inferred_complete_timeline |
| `Action_None` | 168 | 239 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_JetMotion` | 25 | 75 | 51 | inferred_complete_timeline |
| `Action_BallCarry` | 76 | 239 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 157 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 185 | 136 | inferred_complete_timeline |
| `Action_None` | 188 | 239 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 153 | 104 | inferred_complete_timeline |
| `Action_None` | 157 | 163 | 7 | inferred_complete_timeline |
| `Action_None` | 167 | 181 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 79 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 167 | 83 | inferred_complete_timeline |
| `Action_None` | 168 | 239 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 86 | 35 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 87 | 121 | 35 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 128 | 167 | 40 | inferred_complete_timeline |
| `Action_None` | 168 | 239 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_BallSnap` | 50 | 64 | 15 | inferred_complete_timeline |
| `Action_None` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_Toss` | 69 | 75 | 7 | inferred_complete_timeline |
| `Action_None` | 76 | 239 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 75 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 73 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 93 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 98 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 239 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 84 | 35 | inferred_complete_timeline |
| `Action_None` | 86 | 239 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 91 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 239 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 113 | 64 | inferred_complete_timeline |
| `Action_None` | 115 | 119 | 5 | inferred_complete_timeline |
| `Action_None` | 121 | 137 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 77 | 28 | inferred_complete_timeline |
| `Action_None` | 81 | 239 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 239 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 153 | 104 | inferred_complete_timeline |
| `Action_None` | 156 | 227 | 72 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 161 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 198 | 149 | inferred_complete_timeline |
| `Action_None` | 200 | 239 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 239 | 190 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 54–103 | 12 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 72–75 | 4 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 76–239 | 164 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 86–239 | 149 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 89–239 | 151 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 114–115 | 2 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 119–128 | 10 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 156–168 | 13 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 166–239 | 74 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 183–184 | 2 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 185–209 | 25 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 193–239 | 47 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 197–200 | 4 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 218–239 | 19 | 2 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 224–239 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `21` (C)
- ⚠️ `Action_Toss` for actor_track_id `21` (C): Annotated start 68 != Inferred start 69
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '6' (RB) duration 116 frames exceeds threshold 90 frames [start=52, end=167].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (LT) duration 116 frames exceeds threshold 90 frames [start=52, end=167].
- ⚠️ Segment 'Action_ZoneBlock' for track '20' has invalid range: start=52, end=49. Clamping end to start.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [50–64], lower_priority='Action_ZoneBlock' annotated_start=52, effective_Action_ZoneBlock_start=65.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [50–64], lower_priority='Action_SnapReceive' annotated_start=50, effective_Action_SnapReceive_start=65.
- ⚠️ Action 'Action_None' range [50-157] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-75] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-113] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-137] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [52-147] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-79] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-91] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-98] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-161] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-153] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-227] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-185] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-153] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-163] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-181] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-77] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [50-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '20' starts at frame 65, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [65-67] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [87-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-57] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-84] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-75] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-239] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-128] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-168] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-239] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-209] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '36' has 1 frames without a visible bounding box.
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

</details>