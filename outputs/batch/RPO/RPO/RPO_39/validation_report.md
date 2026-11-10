# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_39`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_39/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['LG', 'LT', 'RG', 'RT'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-84] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-140] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-138] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-194] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-173] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-97] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-158] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-156] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-141] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-173] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-186] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-111] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-138] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-14] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-75] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-70] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-108] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-123] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-153] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-162] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-239] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-184] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-140] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-217] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-239] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-201] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-223] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-229] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-214] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-225] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-236] for track '27' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.