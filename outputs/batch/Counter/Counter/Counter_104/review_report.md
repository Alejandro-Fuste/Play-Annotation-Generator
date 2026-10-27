# Play-Annotation-Generator Annotation Review — Counter_104

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_104`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 76
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `3` | `2` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 65 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 63 | START | 63 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `11` | 66 | START | 79 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `5` | `4` | 66 | START | 66 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `6` | `5` | 66 | START | 66 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `3` | `2` | 66 | START | 66 | 106 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `7` | `6` | 66 | START | 66 | 153 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 78 | END | 63 | 78 |
| ✅ EXACT | `Action_BallCarry` | QB | `4` | `3` | 107 | START | 107 | 177 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 153 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_SnapReceive` | 63 | 78 | 16 | inferred_complete_timeline |
| `Action_None` | 79 | 106 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 177 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 97 | 35 | inferred_complete_timeline |
| `Action_None` | 103 | 229 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 170 | 108 | inferred_complete_timeline |
| `Action_None` | 174 | 187 | 14 | inferred_complete_timeline |
| `Action_None` | 189 | 203 | 15 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 239 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 66 | 153 | 88 | inferred_complete_timeline |
| `Action_None` | 154 | 239 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PullBlock` | 66 | 106 | 41 | inferred_complete_timeline |
| `Action_PullBlock` | 112 | 123 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 125 | 144 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 62 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 63 | 78 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 79 | 87 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 93 | 101 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 106 | 135 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_DownBlock` | 66 | 110 | 45 | inferred_complete_timeline |
| `Action_DownBlock` | 129 | 153 | 25 | inferred_complete_timeline |
| `Action_None` | 154 | 161 | 8 | inferred_complete_timeline |
| `Action_None` | 164 | 239 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_DownBlock` | 66 | 137 | 72 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 153 | 15 | inferred_complete_timeline |
| `Action_None` | 154 | 239 | 86 | inferred_complete_timeline |

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
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_None` | 66 | 69 | 4 | inferred_complete_timeline |
| `Action_None` | 74 | 239 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_None` | 70 | 73 | 4 | inferred_complete_timeline |
| `Action_None` | 80 | 86 | 7 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 66 | 4 | inferred_complete_timeline |
| `Action_None` | 72 | 74 | 3 | inferred_complete_timeline |
| `Action_None` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_None` | 114 | 239 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 239 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 131 | 69 | inferred_complete_timeline |
| `Action_None` | 133 | 173 | 41 | inferred_complete_timeline |
| `Action_None` | 177 | 239 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 197 | 135 | inferred_complete_timeline |
| `Action_None` | 199 | 239 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 125 | 63 | inferred_complete_timeline |
| `Action_None` | 135 | 145 | 11 | inferred_complete_timeline |
| `Action_None` | 147 | 239 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_None` | 86 | 239 | 154 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `20` | Position_Unknown | Team_Unknown | 108–239 | 124 | 3 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 138–239 | 101 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 140–239 | 100 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 140–148 | 8 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 150–239 | 87 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 157–165 | 9 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 182–187 | 6 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 201–239 | 37 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [63–78], lower_priority='Action_DownBlock' annotated_start=66, effective_Action_DownBlock_start=79.
- ⚠️ Action 'Action_None' range [63-170] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-187] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-203] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-97] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-229] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [66-106] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [112-123] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [125-144] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [107-177] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [66-110] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [66-137] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-131] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-173] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-125] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-145] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-239] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [79-87] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [89-91] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [93-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [106-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-54] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-86] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-197] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-66] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-239] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-166] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-208] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-181] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-165] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>