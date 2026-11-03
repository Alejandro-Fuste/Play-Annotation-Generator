# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_7`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_7/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-69] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-174] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-168] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-175] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-59] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [104-131] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [133-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-33] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-180] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [101-147] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [150-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-20] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-66] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-89] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-130] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-137] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-154] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-170] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-177] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-162] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-151] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-159] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-171] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '30' has 1 frames without a visible bounding box.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.