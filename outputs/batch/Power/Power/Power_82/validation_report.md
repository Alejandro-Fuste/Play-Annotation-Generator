# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_82`
- **Input XML**: `outputs/batch/Power/Power/Power_82/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 32 |
| Ball Tracks | 1 |
| CSV events parsed | 11 |
| Action Segments inferred | 44 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [13-213] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-25] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-212] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-187] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-233] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-230] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-16] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-173] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [119-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-187] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-198] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-127] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-222] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-129] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-172] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-200] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-197] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '31' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.