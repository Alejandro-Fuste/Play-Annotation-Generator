# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_115`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_115/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_BallCarry' range [173-239] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [262-268] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-247] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-233] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-240] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-255] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-263] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-248] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-257] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-265] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-268] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-189] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [82-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-216] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [82-217] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [220-224] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-242] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-266] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [82-269] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-129] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-233] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-268] for track '28' has 1 frames without a visible bounding box.
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