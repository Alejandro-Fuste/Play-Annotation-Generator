# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_271`
- **Input XML**: `outputs/batch/Power/Power/Power_271/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '13' (C) duration 94 frames exceeds threshold 90 frames [start=115, end=208].
> - Validation warning: Action 'Action_PullBlock' for track '21' (RG) duration 94 frames exceeds threshold 90 frames [start=115, end=208].
> - Action 'Action_PreSnap' range [0-1] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-177] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-299] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-189] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-131] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-154] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-239] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-167] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-188] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-163] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-185] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-203] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [115-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [123-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [139-140] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [144-173] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-276] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-291] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-124] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [115-162] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [178-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-144] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-220] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-226] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-295] for track '30' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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