# Play-Annotation-Generator Annotation Review — JetSweep_128

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_128`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 50
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 156
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | LB2 | defense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Toss` | QB | offense | `18` | `17` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `15` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `20` | `19` | 3 | START | 3 | 11 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 10 | START | 10 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | LB2 | `14` | `13` | 12 | START | 12 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `13` | `12` | 12 | START | 12 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `18` | 12 | START | 24 | 27 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `5` | 12 | START | 12 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `8` | 12 | START | 12 | 65 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 23 | END | 10 | 23 |
| ✅ EXACT | `Action_Toss` | QB | `18` | `17` | 28 | START | 28 | 40 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `20` | `19` | 41 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 99 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 23 | 14 | inferred_complete_timeline |
| `Action_None` | 24 | 27 | 4 | inferred_complete_timeline |
| `Action_Toss` | 28 | 40 | 13 | inferred_complete_timeline |
| `Action_None` | 41 | 76 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 33 | 24 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 67 | 239 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 71 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 47 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 71 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 12 | 44 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 23 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 27 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 86 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 12 | 65 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 99 | 22 | inferred_complete_timeline |
| `Action_None` | 100 | 111 | 12 | inferred_complete_timeline |
| `Action_None` | 116 | 125 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 12 | 28 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 99 | 32 | inferred_complete_timeline |
| `Action_None` | 100 | 107 | 8 | inferred_complete_timeline |
| `Action_None` | 109 | 112 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 65 | 56 | inferred_complete_timeline |
| `Action_None` | 78 | 211 | 134 | inferred_complete_timeline |
| `Action_None` | 218 | 239 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 67 | 58 | inferred_complete_timeline |
| `Action_None` | 71 | 93 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 54 | 45 | inferred_complete_timeline |
| `Action_None` | 56 | 61 | 6 | inferred_complete_timeline |
| `Action_None` | 78 | 84 | 7 | inferred_complete_timeline |
| `Action_None` | 86 | 89 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 49 | 40 | inferred_complete_timeline |
| `Action_None` | 51 | 52 | 2 | inferred_complete_timeline |
| `Action_None` | 54 | 121 | 68 | inferred_complete_timeline |
| `Action_None` | 137 | 140 | 4 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 152 | 4 | inferred_complete_timeline |
| `Action_None` | 154 | 165 | 12 | inferred_complete_timeline |
| `Action_None` | 168 | 174 | 7 | inferred_complete_timeline |
| `Action_None` | 179 | 239 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 84 | 75 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_LeadBlock` | 12 | 42 | 31 | inferred_complete_timeline |
| `Action_LeadBlock` | 61 | 89 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 43 | 34 | inferred_complete_timeline |
| `Action_None` | 56 | 57 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 68 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–212 | 211 | 3 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–76 | 71 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 3–11 | 9 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 18–239 | 131 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 35–68 | 34 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 37–53 | 16 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 60–61 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 60–64 | 5 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 62–63 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 64–134 | 68 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 65–129 | 65 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 67–71 | 5 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 70–158 | 12 | 5 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 72–186 | 112 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 87–128 | 42 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 90–136 | 46 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 126–239 | 33 | 2 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 141–167 | 26 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 146–239 | 85 | 4 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 152–160 | 9 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 156–158 | 3 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 160–165 | 6 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 182–239 | 57 | 2 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 192–239 | 48 | 1 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 201–204 | 4 | 1 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 206–239 | 34 | 1 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 210–215 | 6 | 1 | Undefined position; Undefined team |
| `46` | `63` | Position_Unknown | Team_Unknown | 218–239 | 22 | 1 | Undefined position; Undefined team |
| `47` | `64` | Position_Unknown | Team_Unknown | 220–239 | 13 | 2 | Undefined position; Undefined team |
| `48` | `65` | Position_Unknown | Team_Unknown | 222–239 | 18 | 1 | Undefined position; Undefined team |
| `49` | `66` | Position_Unknown | Team_Unknown | 225–229 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `20` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 86 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 258: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [10–23], lower_priority='Action_ZoneBlock' annotated_start=12, effective_Action_ZoneBlock_start=24.
- ⚠️ Segment 'Action_BallCarry' for track '19' has invalid range: start=41, end=11. Clamping end to start.
- ⚠️ Action 'Action_None' range [10-84] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-47] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-43] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-68] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-68] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [12-44] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-65] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-76] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-71] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [12-65] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-111] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-125] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-67] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-65] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-211] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-54] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-61] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [12-28] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-41] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-99] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-107] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [12-42] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [61-89] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-33] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-49] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-121] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-165] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [24-27] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-86] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [3-11] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-21] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-36] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-68] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-47] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-64] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-123] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-129] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-71] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-132] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-186] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-128] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-133] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-139] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-160] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-167] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-195] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-236] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-160] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-165] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-229] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-229] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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

</details>