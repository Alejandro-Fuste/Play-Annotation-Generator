# Play-Annotation-Generator Annotation Review — SplitZone_83

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_83`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 133
- **Validation Warnings:** 146
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 113
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `22` |
| ❌ MISSING SEGMENT | `Action_SplitBlock` | TE | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | TE | offense | `4` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `9` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 20 | START | 21 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 20 | START | 21 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 20 | START | 21 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 20 | START | 21 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 20 | START | 21 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 20 | START | 21 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 20 | START | 21 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 20 | START | 21 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 20 | START | 21 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 20 | START | 21 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 20 | START | 21 | 104 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 80 | START | 80 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `15` | `15` | 83 | START | 83 | 114 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `17` | 83 | START | 83 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `18` | 83 | START | 118 | 122 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `20` | `20` | 83 | START | 83 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `22` | 83 | START | 83 | 117 |
| ❌ MISSING SEGMENT | `Action_SplitBlock` | TE | `4` | `4` | 86 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | TE | `4` | `4` | 94 | END | 80 | 94 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `6` | 99 | START | 99 | 104 |
| ✅ EXACT | `Action_BallCarry` | RB | `9` | `9` | 105 | START | 105 | 151 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 212 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 98 | 78 | inferred_complete_timeline |
| `Action_Handoff` | 99 | 104 | 6 | inferred_complete_timeline |
| `Action_None` | 105 | 238 | 134 | inferred_complete_timeline |
| `Action_None` | 243 | 280 | 38 | inferred_complete_timeline |
| `Action_None` | 282 | 299 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 21–151
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 104 | 84 | inferred_complete_timeline |
| `Action_BallCarry` | 105 | 151 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_None` | 80 | 299 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_None` | 80 | 299 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_None` | 80 | 299 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_SnapReceive` | 80 | 94 | 15 | inferred_complete_timeline |
| `Action_None` | 95 | 253 | 159 | inferred_complete_timeline |
| `Action_None` | 269 | 275 | 7 | inferred_complete_timeline |
| `Action_None` | 278 | 299 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 21–118
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 82 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 118 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 21–98
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 82 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 98 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_BallSnap` | 80 | 94 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 122 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 131 | 134 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 212 | 76 | inferred_complete_timeline |
| `Action_None` | 213 | 299 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 21–180
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 82 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 117 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 149 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 177 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 21–126
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 82 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 114 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 126 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_None` | 80 | 112 | 33 | inferred_complete_timeline |
| `Action_None` | 118 | 133 | 16 | inferred_complete_timeline |
| `Action_None` | 137 | 140 | 4 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 160 | 9 | inferred_complete_timeline |
| `Action_None` | 167 | 171 | 5 | inferred_complete_timeline |
| `Action_None` | 178 | 299 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 21–133
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_None` | 80 | 101 | 22 | inferred_complete_timeline |
| `Action_None` | 116 | 133 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 21–195
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_None` | 80 | 110 | 31 | inferred_complete_timeline |
| `Action_None` | 116 | 120 | 5 | inferred_complete_timeline |
| `Action_None` | 128 | 134 | 7 | inferred_complete_timeline |
| `Action_None` | 142 | 189 | 48 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 21–188
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_None` | 80 | 98 | 19 | inferred_complete_timeline |
| `Action_None` | 109 | 155 | 47 | inferred_complete_timeline |
| `Action_None` | 163 | 171 | 9 | inferred_complete_timeline |
| `Action_None` | 174 | 181 | 8 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 21–153
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_None` | 80 | 146 | 67 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 21–133
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_None` | 80 | 133 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 21–139
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_None` | 80 | 139 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_None` | 80 | 299 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_None` | 80 | 221 | 142 | inferred_complete_timeline |
| `Action_None` | 232 | 299 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_None` | 80 | 181 | 102 | inferred_complete_timeline |
| `Action_None` | 183 | 205 | 23 | inferred_complete_timeline |
| `Action_None` | 207 | 299 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_None` | 80 | 299 | 220 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 21–32 | 9 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 114–125 | 8 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 116–135 | 17 | 2 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 131–299 | 145 | 8 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 134–299 | 157 | 3 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 136–299 | 159 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 144–186 | 43 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 145–151 | 7 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 152–299 | 132 | 5 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 179–299 | 119 | 3 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 182–192 | 6 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 186–278 | 93 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 189–241 | 27 | 4 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 190–299 | 107 | 2 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 202–299 | 97 | 2 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 203–299 | 89 | 5 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 209–211 | 3 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 217–219 | 3 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 221–227 | 6 | 2 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 228–229 | 2 | 1 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 257–299 | 37 | 2 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 270–271 | 2 | 1 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 289–290 | 2 | 1 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 295–299 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (4 segments found)
- ❌ Missing segment for action `Action_SplitBlock` on target `4` (TE)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 93 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_SplitBlock' for track '4' has invalid range: start=86, end=79. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 130 frames exceeds threshold 90 frames [start=83, end=212].
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [80–94], lower_priority='Action_ZoneBlock' annotated_start=83, effective_Action_ZoneBlock_start=95.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '22' (RG) duration 98 frames exceeds threshold 90 frames [start=83, end=180].
- ⚠️ Action 'Action_None' range [95-253] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-275] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-133] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-238] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-280] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-133] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-221] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [105-151] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-146] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-181] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-205] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-160] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-299] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-299] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-114] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-121] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-171] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-181] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-98] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [80-94] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [131-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-212] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-27] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-32] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-118] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-110] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-134] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-189] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-117] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [119-149] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-177] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [179-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-119] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-135] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-140] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-159] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-176] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-216] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-233] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-185] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-170] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-186] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-151] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-179] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-269] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-250] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-278] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-200] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-208] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-281] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-278] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-242] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-273] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-288] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-268] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>