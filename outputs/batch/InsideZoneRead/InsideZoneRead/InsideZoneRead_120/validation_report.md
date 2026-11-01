# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_120`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_120/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [119–129], lower_priority='Action_ZoneBlock' annotated_start=121, effective_Action_ZoneBlock_start=130.
> - Action 'Action_None' range [119-131] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-161] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-211] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-169] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-238] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-241] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-180] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-231] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-139] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-269] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-178] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-186] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-20] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-174] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-181] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-189] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-209] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-221] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-183] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-217] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-225] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-216] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-220] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-269] for track '24' has 2 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.