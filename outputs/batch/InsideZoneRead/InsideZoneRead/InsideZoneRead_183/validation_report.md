# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_183`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_183/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 366: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-21] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-133] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-168] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-163] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [167-204] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [102-164] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [184-186] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-72] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-193] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-115] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-126] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-143] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-218] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-178] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-140] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-113] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-79] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-183] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-189] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-129] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-180] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-147] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-263] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-189] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-161] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-201] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-172] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-189] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-197] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-217] for track '25' has 1 frames without a visible bounding box.
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
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.