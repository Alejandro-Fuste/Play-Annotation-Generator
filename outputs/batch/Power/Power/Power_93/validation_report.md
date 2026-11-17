# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_93`
- **Input XML**: `outputs/batch/Power/Power/Power_93/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 187: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [6-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-141] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-238] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-184] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-119] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-170] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [81-93] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-92] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-124] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-136] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [81-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [110-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [113-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-147] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-154] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-239] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-137] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [81-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [92-96] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-231] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-46] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-132] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-163] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-188] for track '26' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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