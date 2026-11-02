# Play-Annotation-Generator Annotation Review — JetSweep_119

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_119`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_SealBlock` | TE1 | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 42 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `19` | `18` | 33 | START | 33 | 66 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 43 | START | 43 | 58 |
| ✅ EXACT | `Action_SealBlock` | TE1 | `3` | `2` | 44 | START | 44 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `11` | `10` | 44 | START | 44 | 65 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `12` | `11` | 44 | START | 44 | 89 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `13` | 44 | START | 59 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `16` | `15` | 44 | START | 44 | 60 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `6` | 44 | START | 44 | 89 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 58 | END | 43 | 58 |
| ✅ EXACT | `Action_Toss` | QB | `10` | `9` | 60 | START | 60 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `19` | `18` | 67 | START | 67 | 109 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 89 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_SnapReceive` | 43 | 58 | 16 | inferred_complete_timeline |
| `Action_None` | 59 | 59 | 1 | inferred_complete_timeline |
| `Action_Toss` | 60 | 66 | 7 | inferred_complete_timeline |
| `Action_None` | 67 | 69 | 3 | inferred_complete_timeline |
| `Action_None` | 72 | 108 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–37
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_SealBlock` | 44 | 67 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 84 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 89 | 46 | inferred_complete_timeline |
| `Action_None` | 90 | 108 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 65 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 87 | 8 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_BallSnap` | 43 | 58 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 89 | 31 | inferred_complete_timeline |
| `Action_None` | 90 | 98 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 89 | 46 | inferred_complete_timeline |
| `Action_None` | 90 | 95 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 60 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 89 | 21 | inferred_complete_timeline |
| `Action_None` | 90 | 90 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 192 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 88 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 106 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 151 | 109 | inferred_complete_timeline |
| `Action_None` | 154 | 239 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 102 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 130 | 88 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 79 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 47 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 239 | 197 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 33–218 | 170 | 6 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 34–114 | 36 | 7 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 71–100 | 30 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 74–77 | 4 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 95–175 | 81 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 123–229 | 105 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 142–143 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 159–171 | 13 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 160–201 | 42 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 166–222 | 57 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 195–197 | 3 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 198–239 | 42 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 212–215 | 4 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 221–224 | 4 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 233–239 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 44 != Inferred start 59
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [43–58], lower_priority='Action_ZoneBlock' annotated_start=44, effective_Action_ZoneBlock_start=59.
- ⚠️ Action 'Action_None' range [43-79] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-130] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [44-67] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-102] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-151] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-95] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-47] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [44-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-87] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [43-58] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-88] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [44-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 90, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [90-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-192] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [67-109] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [116-199] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [202-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [211-212] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [216-218] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-59] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-100] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-100] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-175] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-229] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-171] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-201] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-222] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-239] for track '32' has 1 frames without a visible bounding box.
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

</details>