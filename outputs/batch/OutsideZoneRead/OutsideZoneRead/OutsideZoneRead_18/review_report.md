# Play-Annotation-Generator Annotation Review — OutsideZoneRead_18

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_18`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `6` | `6` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 61 |
| ✅ EXACT | `Action_ZoneBlock` | C | `11` | `11` | 54 | START | 54 | 105 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `13` | `13` | 54 | START | 54 | 103 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `2` | 54 | START | 54 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `3` | `3` | 54 | START | 54 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `6` | `6` | 60 | START | 60 | 80 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `7` | `7` | 62 | START | 62 | 69 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `7` | 70 | START | 70 | 87 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 62 | 69 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 70 | 87 | 18 | inferred_complete_timeline |
| `Action_None` | 88 | 115 | 28 | inferred_complete_timeline |
| `Action_None` | 118 | 239 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PressEdge` | 60 | 80 | 21 | inferred_complete_timeline |
| `Action_PressEdge` | 84 | 105 | 22 | inferred_complete_timeline |
| `Action_None` | 106 | 129 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 105 | 52 | inferred_complete_timeline |
| `Action_None` | 106 | 136 | 31 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 148 | 6 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 170 | 15 | inferred_complete_timeline |
| `Action_None` | 174 | 186 | 13 | inferred_complete_timeline |
| `Action_None` | 188 | 195 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 103 | 50 | inferred_complete_timeline |
| `Action_None` | 107 | 111 | 5 | inferred_complete_timeline |
| `Action_None` | 113 | 122 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 105 | 52 | inferred_complete_timeline |
| `Action_None` | 106 | 193 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 101 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 106 | 151 | 46 | inferred_complete_timeline |
| `Action_None` | 160 | 239 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 112 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 82 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 117 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 132 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 197 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 81 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 234 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 124 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 142 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 175 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 195 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 109 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 127 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 143 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–190 | 178 | 4 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–239 | 235 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 8–239 | 232 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 67–239 | 161 | 4 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 78–146 | 69 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 98–239 | 142 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 117–129 | 13 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 118–127 | 10 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 129–239 | 107 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 138–144 | 5 | 2 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 141–155 | 15 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 142–226 | 85 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 158–212 | 55 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 160–239 | 80 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 162–164 | 3 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 169–239 | 70 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 176–193 | 18 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 205–207 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 38: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-124] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-127] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-133] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-142] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-175] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-195] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-136] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-148] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-170] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-186] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-195] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-151] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-110] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-125] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-190] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-109] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-127] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-131] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-143] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [60-80] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-112] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-193] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-234] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-122] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-117] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-132] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-197] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-130] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-141] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-149] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-146] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-129] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-127] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-140] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-155] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-226] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-164] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-172] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-193] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-207] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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