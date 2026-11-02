# Play-Annotation-Generator Annotation Review — JetSweep_243

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_243`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 71
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ EXACT | `Action_JetMotion` | TE1 | offense | `18` | `17` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_LeadBlock` | TE2 | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Toss` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | TE1 | offense | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 21 |
| ✅ EXACT | `Action_JetMotion` | TE1 | `18` | `17` | 20 | START | 20 | 49 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 22 | START | 22 | 45 |
| ✅ EXACT | `Action_LeadBlock` | TE2 | `17` | `16` | 33 | START | 33 | 103 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `12` | `11` | 33 | START | 33 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `18` | 33 | START | 33 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `19` | 33 | START | 33 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 33 | START | 33 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `22` | `21` | 33 | START | 46 | 81 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 45 | END | 22 | 45 |
| ✅ EXACT | `Action_Toss` | QB | `5` | `4` | 49 | START | 49 | 49 |
| ✅ EXACT | `Action_BallCarry` | TE1 | `18` | `17` | 50 | START | 50 | 137 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 103 | BOUNDARY | N/A | N/A |

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
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 45 | 24 | inferred_complete_timeline |
| `Action_None` | 46 | 48 | 3 | inferred_complete_timeline |
| `Action_Toss` | 49 | 49 | 1 | inferred_complete_timeline |
| `Action_None` | 50 | 217 | 168 | inferred_complete_timeline |
| `Action_None` | 219 | 239 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 69 | 48 | inferred_complete_timeline |
| `Action_None` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_None` | 75 | 239 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_JetMotion` | 20 | 49 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 50 | 137 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_LeadBlock` | 33 | 103 | 71 | inferred_complete_timeline |
| `Action_None` | 104 | 160 | 57 | inferred_complete_timeline |
| `Action_None` | 163 | 175 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 88 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 103 | 14 | inferred_complete_timeline |
| `Action_None` | 104 | 239 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 48 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 88 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 22 | 45 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 81 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 91 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 103 | 11 | inferred_complete_timeline |
| `Action_None` | 104 | 239 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 57 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 93 | 61 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 101 | 4 | inferred_complete_timeline |
| `Action_None` | 112 | 155 | 44 | inferred_complete_timeline |
| `Action_None` | 160 | 239 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 68 | 47 | inferred_complete_timeline |
| `Action_None` | 72 | 77 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 219 | 198 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 53 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 213 | 192 | inferred_complete_timeline |
| `Action_None` | 216 | 223 | 8 | inferred_complete_timeline |
| `Action_None` | 225 | 239 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 142 | 121 | inferred_complete_timeline |
| `Action_None` | 144 | 157 | 14 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 167 | 175 | 9 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 112 | 91 | inferred_complete_timeline |
| `Action_None` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 220 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 76 | 55 | inferred_complete_timeline |
| `Action_None` | 80 | 86 | 7 | inferred_complete_timeline |
| `Action_None` | 88 | 90 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 118 | 97 | inferred_complete_timeline |
| `Action_None` | 125 | 161 | 37 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_None` | 200 | 227 | 28 | inferred_complete_timeline |
| `Action_None` | 233 | 238 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 47–239 | 193 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 63–239 | 172 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 81–82 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 96–239 | 144 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 103–239 | 137 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 114–239 | 123 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 124–239 | 113 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 200–238 | 25 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 210–239 | 30 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [22–45], lower_priority='Action_ZoneBlock' annotated_start=33, effective_Action_ZoneBlock_start=46.
- ⚠️ Action 'Action_None' range [22-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-217] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-142] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-157] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-213] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-223] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-76] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-86] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-118] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-161] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-227] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-238] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-220] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [33-57] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-219] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-68] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-77] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-160] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [50-137] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [33-93] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [33-88] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [33-48] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-88] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [46-81] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-91] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-74] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-226] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-185] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-239] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-213] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-238] for track '29' has 2 frames without a visible bounding box.
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

</details>