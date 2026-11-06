# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_35`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_35/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 54 |
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
> - Action 'Action_PreSnap' range [0-133] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-213] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-238] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-134] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-228] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-172] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [174-192] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-221] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-155] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-60] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-224] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-83] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-181] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-212] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-219] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-188] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-196] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-212] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-206] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.