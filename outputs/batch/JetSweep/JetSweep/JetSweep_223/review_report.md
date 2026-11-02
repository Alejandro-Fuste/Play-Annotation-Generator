# Play-Annotation-Generator Annotation Review — JetSweep_223

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_223`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 88
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
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `5` | `4` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE2 | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Toss` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `16` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 82 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `5` | `4` | 37 | START | 37 | 101 |
| ✅ EXACT | `Action_BallSnap` | RG | `20` | `19` | 83 | START | 83 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE2 | `11` | `10` | 85 | START | 85 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `0` | 85 | START | 85 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `16` | 85 | START | 85 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `2` | `1` | 85 | START | 85 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `19` | 85 | START | 85 | 109 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `21` | `20` | 85 | START | 85 | 198 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 93 | END | 83 | 93 |
| ✅ EXACT | `Action_Toss` | QB | `15` | `14` | 100 | START | 100 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `5` | `4` | 102 | START | 102 | 176 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 198 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_SnapReceive` | 83 | 93 | 11 | inferred_complete_timeline |
| `Action_None` | 94 | 99 | 6 | inferred_complete_timeline |
| `Action_Toss` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 102 | 239 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 218 | 136 | inferred_complete_timeline |
| `Action_None` | 220 | 223 | 4 | inferred_complete_timeline |
| `Action_None` | 225 | 239 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_JetMotion` | 37 | 101 | 65 | inferred_complete_timeline |
| `Action_BallCarry` | 102 | 176 | 75 | inferred_complete_timeline |
| `Action_BallCarry` | 183 | 223 | 41 | inferred_complete_timeline |
| `Action_BallCarry` | 227 | 235 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 192 | 110 | inferred_complete_timeline |
| `Action_None` | 203 | 205 | 3 | inferred_complete_timeline |
| `Action_None` | 207 | 218 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 189 | 107 | inferred_complete_timeline |
| `Action_None` | 191 | 201 | 11 | inferred_complete_timeline |
| `Action_None` | 203 | 239 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_LeadBlock` | 85 | 189 | 105 | inferred_complete_timeline |
| `Action_LeadBlock` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 239 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 198 | 114 | inferred_complete_timeline |
| `Action_None` | 199 | 239 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 121 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 198 | 76 | inferred_complete_timeline |
| `Action_None` | 199 | 239 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 101 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 129 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_BallSnap` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 109 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 187 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 189 | 198 | 10 | inferred_complete_timeline |
| `Action_None` | 199 | 199 | 1 | inferred_complete_timeline |
| `Action_None` | 202 | 204 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 198 | 114 | inferred_complete_timeline |
| `Action_None` | 199 | 239 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 239 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 124 | 42 | inferred_complete_timeline |
| `Action_None` | 126 | 201 | 76 | inferred_complete_timeline |
| `Action_None` | 204 | 239 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 115 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 222 | 140 | inferred_complete_timeline |
| `Action_None` | 224 | 226 | 3 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 100 | 18 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 199 | 117 | inferred_complete_timeline |
| `Action_None` | 201 | 237 | 37 | inferred_complete_timeline |
| `Action_None` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 193 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 82 | 79 | inferred_complete_timeline |
| `Action_None` | 83 | 239 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 169 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 187 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 160 | 78 | inferred_complete_timeline |
| `Action_None` | 169 | 235 | 67 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `31` | Position_Unknown | Team_Unknown | 116–239 | 124 | 1 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 125–126 | 2 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 125–239 | 112 | 3 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 125–126 | 2 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 137–239 | 102 | 2 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 165–207 | 33 | 2 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 183–239 | 32 | 5 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 201–239 | 39 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 212–239 | 14 | 3 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 230–239 | 8 | 2 | Undefined position; Undefined team |
| `32` | `52` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |
| `33` | `53` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (LT) duration 114 frames exceeds threshold 90 frames [start=85, end=198].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LG) duration 114 frames exceeds threshold 90 frames [start=85, end=198].
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '10' (TE2) duration 114 frames exceeds threshold 90 frames [start=85, end=198].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (RG) duration 114 frames exceeds threshold 90 frames [start=85, end=198].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RT) duration 114 frames exceeds threshold 90 frames [start=85, end=198].
- ⚠️ Action 'Action_ZoneBlock' range [85-198] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-121] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-169] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-192] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-218] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [102-176] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [183-223] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [227-235] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-115] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-124] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-201] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-199] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-218] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [85-189] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [191-192] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-193] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-222] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-160] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-235] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-189] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-201] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-239] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-101] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-129] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-187] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-109] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [113-187] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [189-198] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 199, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [199-199] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-224] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-192] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-187] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-201] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-221] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-223] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '31' has 1 frames without a visible bounding box.
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

</details>