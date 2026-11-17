# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_34`
- **Input XML**: `outputs/batch/Power/Power/Power_34/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [11-246] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-201] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-191] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-315] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-324] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [168-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-204] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-229] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-170] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-187] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-204] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-31] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [168-171] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-199] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-175] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-206] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-203] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-273] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-241] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-321] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-290] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-297] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-313] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-309] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-311] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-326] for track '32' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.