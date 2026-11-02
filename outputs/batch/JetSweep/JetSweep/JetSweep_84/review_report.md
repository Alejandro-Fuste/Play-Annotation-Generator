# Play-Annotation-Generator Annotation Review — JetSweep_84

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_84`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 63
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 26
- **Exact Matches:** 10
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `2` | `1` |
| ✅ EXACT | `Action_BallSnap` | DT2 | defense | `15` | `14` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `4` | `3` |
| ✅ EXACT | `Action_SealBlock` | TE2 | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Toss` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `20` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 0 | START | 0 | 63 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `2` | `1` | 26 | START | 26 | 84 |
| ✅ EXACT | `Action_BallSnap` | DT2 | `15` | `14` | 57 | START | 57 | 69 |
| ✅ EXACT | `Action_LeadBlock` | RB | `4` | `3` | 64 | START | 64 | 127 |
| ✅ EXACT | `Action_SealBlock` | TE2 | `6` | `5` | 64 | START | 64 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 64 | START | 64 | 69 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `13` | 64 | START | 64 | 81 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `16` | 64 | START | 64 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 64 | START | 64 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `22` | `21` | 64 | START | 64 | 101 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 69 | END | 57 | 69 |
| ✅ EXACT | `Action_Toss` | QB | `5` | `4` | 78 | START | 78 | 84 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `14` | `13` | 82 | START | 82 | 127 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `2` | `1` | 85 | START | 85 | 186 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 127 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_SnapReceive` | 57 | 69 | 13 | inferred_complete_timeline |
| `Action_None` | 70 | 77 | 8 | inferred_complete_timeline |
| `Action_Toss` | 78 | 84 | 7 | inferred_complete_timeline |
| `Action_None` | 85 | 210 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_LeadBlock` | 64 | 127 | 64 | inferred_complete_timeline |
| `Action_None` | 128 | 210 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_JetMotion` | 26 | 84 | 59 | inferred_complete_timeline |
| `Action_BallCarry` | 85 | 186 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 210 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 210 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_SealBlock` | 64 | 96 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 101 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 127 | 9 | inferred_complete_timeline |
| `Action_None` | 128 | 175 | 48 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 198 | 7 | inferred_complete_timeline |
| `Action_None` | 200 | 210 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 78 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 81 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 69 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 127 | 54 | inferred_complete_timeline |
| `Action_None` | 128 | 210 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 109 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 81 | 18 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 82 | 127 | 46 | inferred_complete_timeline |
| `Action_None` | 128 | 210 | 83 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 76 | 20 | inferred_complete_timeline |
| `Action_None` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 210 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 210 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 96 | 40 | inferred_complete_timeline |
| `Action_None` | 103 | 115 | 13 | inferred_complete_timeline |
| `Action_None` | 117 | 210 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_BallSnap` | 57 | 69 | 13 | inferred_complete_timeline |
| `Action_None` | 70 | 84 | 15 | inferred_complete_timeline |
| `Action_None` | 94 | 115 | 22 | inferred_complete_timeline |
| `Action_None` | 123 | 130 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 210 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 210 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 210 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 210 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 210 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 210 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 183 | 127 | inferred_complete_timeline |
| `Action_None` | 188 | 190 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 107–210 | 104 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 110–210 | 101 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 126–135 | 9 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 135–138 | 4 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 136–207 | 58 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 172–188 | 17 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 48 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [57-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [85-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [64-96] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-183] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-69] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-115] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-115] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-210] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-76] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-107] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-175] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-198] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-156] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-179] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-207] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '28' has 1 frames without a visible bounding box.
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

</details>