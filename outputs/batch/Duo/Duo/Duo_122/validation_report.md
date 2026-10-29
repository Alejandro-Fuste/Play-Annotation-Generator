# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_122`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_122/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 31 |
| Ball Tracks | 1 |
| CSV events parsed | 15 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ComboBlock' for track '15' has invalid range: start=171, end=117. Clamping end to start.
> - Segment 'Action_ComboBlock' for track '17' has invalid range: start=171, end=150. Clamping end to start.
> - Segment 'Action_ComboBlock' for track '21' has invalid range: start=171, end=123. Clamping end to start.
> - Action 'Action_PreSnap' range [0-136] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-209] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-161] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-192] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-209] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-164] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-169] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-145] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-129] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-139] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-209] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-209] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-159] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-167] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [171-207] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-37] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-117] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-129] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-145] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-158] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-40] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-55] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-123] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-115] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-146] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-165] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-164] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-173] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-209] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-176] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-181] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-191] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-199] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-209] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-196] for track '31' has 1 frames without a visible bounding box.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.