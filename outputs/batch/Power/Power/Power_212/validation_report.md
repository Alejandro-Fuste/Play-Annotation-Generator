# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_212`
- **Input XML**: `outputs/batch/Power/Power/Power_212/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 426: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-310] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-281] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-228] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-50] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-171] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-86] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [172-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [244-247] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [172-251] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-202] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-276] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-286] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-58] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-242] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-57] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-164] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-208] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-252] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-310] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-260] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-279] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-312] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-303] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-325] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-315] for track '26' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.