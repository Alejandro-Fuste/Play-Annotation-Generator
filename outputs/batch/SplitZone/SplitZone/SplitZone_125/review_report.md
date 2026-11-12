# Play-Annotation-Generator Annotation Review — SplitZone_125

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_125`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 127
- **Validation Warnings:** 149
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 106
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `16` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `13` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 31 | START | 31 | 39 |
| ✅ EXACT | `Action_SplitBlock` | HB | `13` | `13` | 34 | START | 34 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `14` | `14` | 34 | START | 34 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `18` | 34 | START | 34 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 34 | START | 40 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 34 | START | 34 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `21` | 34 | START | 34 | 81 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 39 | END | 31 | 39 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `17` | 47 | START | 47 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `16` | `16` | 53 | START | 53 | 74 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 149 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 39 | 9 | inferred_complete_timeline |
| `Action_None` | 40 | 46 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 47 | 52 | 6 | inferred_complete_timeline |
| `Action_None` | 53 | 55 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_BallCarry` | 53 | 74 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 80 | 83 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 112 | 210 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_SplitBlock` | 34 | 149 | 116 | inferred_complete_timeline |
| `Action_None` | 150 | 174 | 25 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 210 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 210 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 98 | 68 | inferred_complete_timeline |
| `Action_None` | 109 | 120 | 12 | inferred_complete_timeline |
| `Action_None` | 124 | 129 | 6 | inferred_complete_timeline |
| `Action_None` | 131 | 177 | 47 | inferred_complete_timeline |
| `Action_None` | 179 | 210 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 60 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 98 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 149 | 33 | inferred_complete_timeline |
| `Action_None` | 150 | 210 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 36 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 44 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_BallSnap` | 31 | 39 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 47 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 90 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 149 | 8 | inferred_complete_timeline |
| `Action_None` | 150 | 155 | 6 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 39 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 52 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 57 | 68 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 117 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 81 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 149 | 67 | inferred_complete_timeline |
| `Action_None` | 150 | 154 | 5 | inferred_complete_timeline |
| `Action_None` | 160 | 202 | 43 | inferred_complete_timeline |
| `Action_None` | 204 | 209 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 118 | 88 | inferred_complete_timeline |
| `Action_None` | 120 | 210 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 90 | 60 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 96 | 210 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 114 | 84 | inferred_complete_timeline |
| `Action_None` | 118 | 121 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 57 | 27 | inferred_complete_timeline |
| `Action_None` | 59 | 62 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 122 | 92 | inferred_complete_timeline |
| `Action_None` | 125 | 194 | 70 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 74 | 44 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 125 | 95 | inferred_complete_timeline |
| `Action_None` | 127 | 139 | 13 | inferred_complete_timeline |
| `Action_None` | 143 | 206 | 64 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 210 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 107 | 77 | inferred_complete_timeline |
| `Action_None` | 109 | 124 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 114 | 84 | inferred_complete_timeline |
| `Action_None` | 117 | 159 | 43 | inferred_complete_timeline |
| `Action_None` | 161 | 210 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 210 | 180 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 32–33 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 54–210 | 157 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 54–55 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 67–72 | 6 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 78–107 | 28 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 87–210 | 119 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 94–210 | 105 | 5 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 99–112 | 14 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 102–165 | 64 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 112–117 | 6 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 122–131 | 10 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 123–210 | 85 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 134–135 | 2 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 135–138 | 4 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 138–153 | 14 | 2 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 141–147 | 6 | 2 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 163–210 | 37 | 3 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 178–203 | 21 | 2 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 180–204 | 25 | 1 | Undefined position; Undefined team |
| `42` | `48` | Position_Unknown | Team_Unknown | 191–192 | 2 | 1 | Undefined position; Undefined team |
| `43` | `50` | Position_Unknown | Team_Unknown | 203–208 | 5 | 2 | Undefined position; Undefined team |
| `44` | `51` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 98 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (LT) duration 116 frames exceeds threshold 90 frames [start=34, end=149].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (C) duration 116 frames exceeds threshold 90 frames [start=34, end=149].
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [31–39], lower_priority='Action_ZoneBlock' annotated_start=34, effective_Action_ZoneBlock_start=40.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 116 frames exceeds threshold 90 frames [start=34, end=149].
- ⚠️ Action 'Action_None' range [31-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-98] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-177] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-194] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-74] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-107] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-124] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-125] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-206] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-90] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-114] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-114] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-118] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-210] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [107-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-210] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-57] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-62] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [53-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [80-83] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-55] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-36] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-39] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [43-44] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-94] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-39] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [48-52] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [57-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-117] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-81] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-202] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-209] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-33] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-72] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-96] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-107] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-174] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-105] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-117] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-112] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-165] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-117] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-131] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-147] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-203] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-204] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '44' has 1 frames without a visible bounding box.
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

</details>