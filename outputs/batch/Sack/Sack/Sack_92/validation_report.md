# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_92`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_92/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 8 |
| Action Segments inferred | 50 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 186: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-159] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-203] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-209] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-145] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-189] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-165] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-181] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-191] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-198] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [125-167] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [169-209] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-200] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-205] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-96] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-70] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-79] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-90] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-98] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-151] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-182] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-210] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-144] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-169] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-158] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-169] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-162] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-164] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-169] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-210] for track '21' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.