# Play-Annotation-Generator Annotation Review — JetSweep_177

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_177`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_FirstDown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 63
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
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ EXACT | `Action_JetMotion` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_LeadBlock` | TE1 | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Toss` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `20` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 17 |
| ✅ EXACT | `Action_JetMotion` | RT | `1` | `0` | 1 | START | 1 | 17 |
| ✅ EXACT | `Action_BallSnap` | RG | `22` | `21` | 11 | START | 11 | 17 |
| ✅ EXACT | `Action_LeadBlock` | TE1 | `3` | `2` | 18 | START | 18 | 85 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `0` | 18 | START | 18 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 18 | START | 18 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `17` | 18 | START | 18 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 18 | START | 18 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 18 | START | 18 | 22 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 24 | END | 11 | 24 |
| ✅ EXACT | `Action_Toss` | QB | `12` | `11` | 29 | START | 29 | 39 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `11` | `10` | 40 | START | 40 | 150 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 85 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 24 | 14 | inferred_complete_timeline |
| `Action_None` | 25 | 28 | 4 | inferred_complete_timeline |
| `Action_Toss` | 29 | 39 | 11 | inferred_complete_timeline |
| `Action_None` | 40 | 150 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 125 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_BallCarry` | 40 | 150 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 150 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_LeadBlock` | 18 | 85 | 68 | inferred_complete_timeline |
| `Action_None` | 86 | 150 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 60 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 23 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 65 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 63 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 85 | 21 | inferred_complete_timeline |
| `Action_None` | 86 | 99 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 33 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 85 | 17 | inferred_complete_timeline |
| `Action_None` | 86 | 150 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 17 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 22 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 42 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 56 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 85 | 26 | inferred_complete_timeline |
| `Action_None` | 86 | 150 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_JetMotion` | 1 | 17 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 34 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 150 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 150 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 59 | 49 | inferred_complete_timeline |
| `Action_None` | 61 | 102 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 150 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 88 | 78 | inferred_complete_timeline |
| `Action_None` | 91 | 150 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 92 | 82 | inferred_complete_timeline |
| `Action_None` | 102 | 150 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 150 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 73 | 63 | inferred_complete_timeline |
| `Action_None` | 91 | 150 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 150 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 150 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 150 | 140 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 37–47 | 11 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 46–150 | 101 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 64–68 | 4 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 74–150 | 77 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 87–150 | 63 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 97–150 | 51 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 98–150 | 52 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 137–150 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 46 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_ZoneBlock' range [18-34] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-92] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-88] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-59] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-102] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [40-150] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-33] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-73] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-125] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-23] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-65] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-63] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-99] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-60] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-150] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-22] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-42] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-47] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-50] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-125] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-150] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-134] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-106] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-150] for track '29' has 1 frames without a visible bounding box.
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

</details>